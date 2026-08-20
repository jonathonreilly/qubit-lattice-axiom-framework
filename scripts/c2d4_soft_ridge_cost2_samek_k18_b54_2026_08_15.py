#!/usr/bin/env python3
"""Score same-k reverse at k=18 under s2 on B_54(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/C2D4_SOFT_RIDGE_COST2_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=18 under the named c2d4-plus-soft-ridge "
    "hop-cost on B_54(0) is reported. Displayed, not adopted."
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


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) > max(abs(coord) for coord in v):
            return 3
    return 1


def d3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if (
            max(abs(coord) for coord in w) > max(abs(coord) for coord in v)
            and max(abs(coord) for coord in v) >= 3
        ):
            return 3
    return 1


def d4_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if (
            max(abs(coord) for coord in w) > max(abs(coord) for coord in v)
            and max(abs(coord) for coord in v) >= 4
        ):
            return 3
    return 1


def c2d3_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if (
            max(abs(coord) for coord in w) > max(abs(coord) for coord in v)
            and max(abs(coord) for coord in v) >= 3
        ):
            return 2
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


def ridge_stay(v: tuple[int, int, int], w: tuple[int, int, int]) -> bool:
    return (
        support_size(v) == 3
        and support_size(w) == 3
        and sum(abs(coord) == 1 for coord in w) == 2
    )


def s2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if mu_cost(v, w) == 3:
        return 3
    if ridge_stay(v, w) or c2d4_cost(v, w) == 2:
        return 2
    return 1


def path_cost(path: list[tuple[int, int, int]]) -> int:
    return sum(s2_cost(a, b) for a, b in zip(path, path[1:]))


def dijkstra_s2(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + s2_cost(v, w)
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
        "s2 is not written into Admissibility",
        "Do not write s2 into Admissibility" in note
        and "Do not write `s2` into Admissibility" in note,
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

    sites = ball(54)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_s2(sites)
    t1800 = dist[(18, 0, 0)]
    t181818 = dist[(18, 18, 18)]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t121 = dist[(1, 2, 1)]
    t211 = dist[(2, 1, 1)]
    t221 = dist[(2, 2, 1)]
    t222 = dist[(2, 2, 2)]
    t5400 = dist[(54, 0, 0)]
    t5100 = dist[(51, 0, 0)]
    t320 = dist[(3, 2, 0)]
    t420 = dist[(4, 2, 0)]
    t520 = dist[(5, 2, 0)]
    reverse = 3 * t1800 * t1800 > t181818 * t181818
    reverse_k1 = 3 * t100 * t100 > t111 * t111
    axis_sq = t1800 * t1800
    body_sq = t181818 * t181818
    axis_prod = 3 * axis_sq

    axis_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1)]
    axis_witness.extend((x, 2, 1) for x in range(2, 19))
    axis_witness.extend([(18, 1, 1), (18, 1, 0), (18, 0, 0)])
    body_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2)]
    body_witness.extend((x, 2, 2) for x in range(3, 19))
    body_witness.extend((18, y, 2) for y in range(3, 19))
    body_witness.extend((18, 18, z) for z in range(3, 19))
    skip_witness = [
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 2, 0),
        (2, 2, 0),
        (3, 2, 0),
        (4, 2, 0),
    ]
    fire_witness = skip_witness + [(5, 2, 0)]
    skip_hop = ((3, 2, 0), (4, 2, 0))
    fire_hop = ((4, 2, 0), (5, 2, 0))
    unit_out_face = ((1, 1, 0), (2, 1, 0))
    ridge_hop = ((1, 1, 1), (2, 1, 1))
    ridge_hop_alt = ((1, 1, 1), (1, 2, 1))
    axis_leave_ridge = ((18, 2, 1), (18, 1, 1))

    print(f"n_sites {len(sites)}")
    print(f"t(18,0,0) {t1800}")
    print(f"t(18,18,18) {t181818}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"t(18,0,0)^2/324 {axis_sq}/324")
    print(f"t(18,18,18)^2/972 {body_sq}/972")
    print(f"3 t(18,0,0)^2 {axis_prod}")
    print(f"t(18,18,18)^2 {body_sq}")
    print(f"reverse {reverse}")
    print(f"t(54,0,0) {t5400}")
    print(f"t(51,0,0) {t5100}")
    print(f"t(3,2,0) {t320}")
    print(f"t(4,2,0) {t420}")
    print(f"t(5,2,0) {t520}")
    print(f"t(1,2,1) {t121}")
    print(f"t(2,1,1) {t211}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "theorem-1",
        "t(18,0,0)=32 and t(18,18,18)=57 match named witnesses",
        t1800 == 32
        and t181818 == 57
        and t1800 == path_cost(axis_witness)
        and t181818 == path_cost(body_witness),
    )
    checks.check(
        "reverse-k18",
        "t(18,0,0)^2 / 324 > t(18,18,18)^2 / 972 does not hold",
        (not reverse)
        and axis_prod == 3072
        and body_sq == 3249
        and "3072 < 3249" in note
        and "inequality does not hold" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b54",
        "B_54(0) has 215929 sites and 215928 nonzero sites",
        len(sites) == 215929 and len(nonzero) == 215928 and all(l1(v) <= 54 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_54(0) is reached",
        len(dist) == 215929,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        f"t(18,0,0) = {t1800}" in note
        and f"t(18,18,18) = {t181818}" in note
        and "`(18,0,0)`" in note
        and "`(18,18,18)`" in note
        and "`32`" in note
        and "`57`" in note,
    )
    checks.check(
        "note-records-reverse-product",
        "note records the integer reverse comparison",
        f"{axis_prod} < {body_sq}" in note
        and f"{axis_sq}/324" in note
        and f"{body_sq}/972" in note,
    )
    checks.check(
        "soft-ridge-stay-at-2",
        "s2 prices ρ3 ridge-stay (1,1,1)->(2,1,1) at 2",
        s2_cost(*ridge_hop) == 2
        and s2_cost(*ridge_hop_alt) == 2
        and s2_cost(*axis_leave_ridge) == 2
        and rho3_cost(*ridge_hop) == 3
        and c2d4_cost(*ridge_hop) == 3
        and mu_cost(*ridge_hop) == 1
        and ridge_stay(*ridge_hop)
        and t121 == 7
        and t211 == 7
        and t221 == 8
        and t222 == 9
        and "(1,1,1) → (2,1,1)" in note
        and "`t(1,2,1) = 7`" in note
        and "`t(2,1,1) = 7`" in note,
    )
    checks.check(
        "skips-early-out-face",
        "s2 skips (3,2,0)->(4,2,0); that hop is cost 1",
        s2_cost(*skip_hop) == 1
        and c2d4_cost(*skip_hop) == 1
        and d4_cost(*skip_hop) == 1
        and d3_cost(*skip_hop) == 3
        and c2d3_cost(*skip_hop) == 2
        and omega_cost(*skip_hop) == 3
        and rho3_cost(*skip_hop) == 1
        and max(abs(c) for c in skip_hop[0]) == 3
        and t320 == 9
        and t420 == 10
        and path_cost(skip_witness) == 10
        and "(3,2,0) → (4,2,0)" in note
        and "`t(3,2,0) = 9`" in note
        and "`t(4,2,0) = 10`" in note,
    )
    checks.check(
        "fires-max4-out-face-at-2",
        "s2 keeps c2d4 fire (4,2,0)->(5,2,0) at cost 2",
        s2_cost(*fire_hop) == 2
        and c2d4_cost(*fire_hop) == 2
        and d4_cost(*fire_hop) == 3
        and rho3_cost(*fire_hop) == 1
        and omega_cost(*fire_hop) == 3
        and max(abs(c) for c in fire_hop[0]) == 4
        and t520 == path_cost(fire_witness)
        and path_cost(fire_witness) == 12
        and "(4,2,0) → (5,2,0)" in note
        and "`t(5,2,0) = 12`" in note,
    )
    checks.check(
        "unit-out-face-by-mu",
        "unit-out-face (1,1,0)->(2,1,0) stays s2=3 by corridor-slide",
        s2_cost(*unit_out_face) == 3
        and mu_cost(*unit_out_face) == 3
        and rho3_cost(*unit_out_face) == 3
        and c2d4_cost(*unit_out_face) == 3
        and "(1,1,0) → (2,1,0)" in note,
    )
    checks.check(
        "not-leftover-of-c2d4",
        "ridge-stay is s2=2 and c2d4=3",
        s2_cost(*ridge_hop) == 2
        and c2d4_cost(*ridge_hop) == 3
        and "cannot price the soft ridge-stay" in note
        and "not leftover of `c2d4`" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "ridge-stay is s2=2 and ρ3=3",
        s2_cost(*ridge_hop) == 2
        and rho3_cost(*ridge_hop) == 3
        and "not leftover of `ρ3`" in note
        and "cost `2` (not `3`)" in note,
    )
    checks.check(
        "not-leftover-of-b51",
        "(18,18,18) lies outside B_51(0) and the note says so",
        l1((18, 18, 18)) == 54
        and (18, 18, 18) in dist
        and t5400 == 73
        and t5100 == 65
        and f"t(54,0,0) = {t5400}" in note
        and f"t(51,0,0) = {t5100}" in note
        and "absent from `B_51(0)`" in note
        and "not leftover of the `B_51(0)` times" in note,
    )
    checks.check(
        "k1-kept",
        "the same Dijkstra keeps t(1,0,0)=3 versus t(1,1,1)=5",
        t100 == 3
        and t111 == 5
        and reverse_k1
        and "t(1,0,0) = 3" in note
        and "t(1,1,1) = 5" in note,
    )
    checks.check(
        "witness-arrivals",
        "named axis and body walks realize the computed arrivals",
        path_cost(axis_witness) == t1800
        and path_cost(body_witness) == t181818
        and axis_witness[-1] == (18, 0, 0)
        and body_witness[-1] == (18, 18, 18)
        and all(l1(v) <= 54 for v in axis_witness)
        and all(l1(v) <= 54 for v in body_witness),
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1; ridge-stay costs 2",
        s2_cost((0, 0, 0), (1, 0, 0)) == 3
        and s2_cost((1, 0, 0), (2, 0, 0)) == 3
        and s2_cost((1, 0, 0), (1, 1, 0)) == 1
        and s2_cost((1, 1, 0), (1, 1, 1)) == 1
        and s2_cost((1, 1, 0), (1, 0, 0)) == 3
        and s2_cost((1, 1, 1), (2, 1, 1)) == 2
        and s2_cost((2, 1, 1), (2, 2, 1)) == 1
        and s2_cost((2, 2, 2), (3, 2, 2)) == 1
        and s2_cost((18, 18, 17), (18, 18, 18)) == 1
        and s2_cost((4, 1, 0), (5, 1, 0)) == 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "s2(v→w)" not in axiom
        and "c2d4(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
