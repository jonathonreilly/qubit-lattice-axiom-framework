#!/usr/bin/env python3
"""Score same-k reverse at k=18 under c2d4 on B_54(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COST2_MAX4_OUT_FACE_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_MAX4_OUT_FACE_SAMEK_K18_B54_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=18 under the named cost-2 max≥4 "
    "out-face hop-cost on B_54(0) is reported. Displayed, not adopted."
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


def path_cost(path: list[tuple[int, int, int]]) -> int:
    return sum(c2d4_cost(a, b) for a, b in zip(path, path[1:]))


def dijkstra_c2d4(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + c2d4_cost(v, w)
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
        "c2d4 is not written into Admissibility",
        "Do not write c2d4 into Admissibility" in note
        and "Do not write `c2d4` into Admissibility" in note,
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
    dist = dijkstra_c2d4(sites)
    t1800 = dist[(18, 0, 0)]
    t181818 = dist[(18, 18, 18)]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t1400 = dist[(14, 0, 0)]
    t141414 = dist[(14, 14, 14)]
    t1500 = dist[(15, 0, 0)]
    t151515 = dist[(15, 15, 15)]
    t1600 = dist[(16, 0, 0)]
    t161616 = dist[(16, 16, 16)]
    t1700 = dist[(17, 0, 0)]
    t171717 = dist[(17, 17, 17)]
    t5400 = dist[(54, 0, 0)]
    t5100 = dist[(51, 0, 0)]
    t320 = dist[(3, 2, 0)]
    t420 = dist[(4, 2, 0)]
    t520 = dist[(5, 2, 0)]
    reverse = 3 * t1800 * t1800 > t181818 * t181818
    reverse_k1 = 3 * t100 * t100 > t111 * t111
    reverse_k14 = 3 * t1400 * t1400 > t141414 * t141414
    reverse_k15 = 3 * t1500 * t1500 > t151515 * t151515
    reverse_k16 = 3 * t1600 * t1600 > t161616 * t161616
    reverse_k17 = 3 * t1700 * t1700 > t171717 * t171717
    axis_sq = t1800 * t1800
    body_sq = t181818 * t181818
    axis_prod = 3 * axis_sq

    axis_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 2, 1)]
    axis_witness.extend((x, 2, 1) for x in range(2, 19))
    axis_witness.extend([(18, 2, 0), (18, 1, 0), (18, 0, 0)])
    body_witness = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 2, 0), (2, 2, 0), (2, 2, 1)]
    body_witness.extend((2, 2, z) for z in range(2, 19))
    body_witness.extend((2, y, 18) for y in range(3, 19))
    body_witness.extend((x, 18, 18) for x in range(3, 19))
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

    print(f"n_sites {len(sites)}")
    print(f"t(18,0,0) {t1800}")
    print(f"t(18,18,18) {t181818}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"t(14,0,0) {t1400}")
    print(f"t(14,14,14) {t141414}")
    print(f"t(15,0,0) {t1500}")
    print(f"t(15,15,15) {t151515}")
    print(f"t(16,0,0) {t1600}")
    print(f"t(16,16,16) {t161616}")
    print(f"t(17,0,0) {t1700}")
    print(f"t(17,17,17) {t171717}")
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
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "theorem-1",
        "t(18,0,0)=34 and t(18,18,18)=58 match named witnesses",
        t1800 == 34
        and t181818 == 58
        and t1800 == path_cost(axis_witness)
        and t181818 == path_cost(body_witness),
    )
    checks.check(
        "reverse-k18",
        "t(18,0,0)^2 / 324 > t(18,18,18)^2 / 972 holds",
        reverse
        and axis_prod == 3468
        and body_sq == 3364
        and "3468 > 3364" in note
        and "inequality holds" in note,
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
        and "`34`" in note
        and "`58`" in note,
    )
    checks.check(
        "note-records-reverse-product",
        "note records the integer reverse comparison",
        f"{axis_prod} > {body_sq}" in note
        and f"{axis_sq}/324" in note
        and f"{body_sq}/972" in note,
    )
    checks.check(
        "skips-early-out-face",
        "c2d4 skips (3,2,0)->(4,2,0); that hop is cost 1",
        c2d4_cost(*skip_hop) == 1
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
        "c2d4 fires (4,2,0)->(5,2,0) at cost 2",
        c2d4_cost(*fire_hop) == 2
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
        "unit-out-face (1,1,0)->(2,1,0) is already ρ3=3 by corridor-slide",
        c2d4_cost(*unit_out_face) == 3
        and rho3_cost(*unit_out_face) == 3
        and mu_cost(*unit_out_face) == 3
        and "(1,1,0) → (2,1,0)" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "max≥4 out-face is c2d4=2 and ρ3=1",
        c2d4_cost(*fire_hop) == 2
        and rho3_cost(*fire_hop) == 1
        and "cannot price max≥4 out-face" in note,
    )
    checks.check(
        "not-leftover-of-d4",
        "d4 prices max≥4 out-face at 3 while c2d4 prices it at 2",
        c2d4_cost(*fire_hop) == 2
        and d4_cost(*fire_hop) == 3
        and t520 == 12
        and "not leftover of `d4`" in note
        and "cost `2` (not `3`)" in note,
    )
    checks.check(
        "not-leftover-of-b51",
        "(18,18,18) lies outside B_51(0) and the note says so",
        l1((18, 18, 18)) == 54
        and (18, 18, 18) in dist
        and t5400 == 75
        and t5100 == 67
        and f"t(54,0,0) = {t5400}" in note
        and f"t(51,0,0) = {t5100}" in note
        and "absent from `B_51(0)`" in note
        and "not leftover of the `B_51(0)` times" in note,
    )
    checks.check(
        "k14-restored",
        "the same Dijkstra restores t(14,0,0)=30 versus t(14,14,14)=46",
        t1400 == 30
        and t141414 == 46
        and reverse_k14
        and "t(14,0,0) = 30" in note
        and "t(14,14,14) = 46" in note,
    )
    checks.check(
        "k17-kept",
        "the same Dijkstra keeps t(17,0,0)=33 versus t(17,17,17)=55",
        t1700 == 33
        and t171717 == 55
        and reverse_k17
        and reverse_k16
        and reverse_k15
        and reverse_k1
        and t1600 == 32
        and t161616 == 52
        and t1500 == 31
        and t151515 == 49
        and t100 == 3
        and t111 == 5
        and "t(17,0,0) = 33" in note
        and "t(17,17,17) = 55" in note
        and "t(16,0,0) = 32" in note
        and "t(16,16,16) = 52" in note
        and "t(15,0,0) = 31" in note
        and "t(15,15,15) = 49" in note
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
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        c2d4_cost((0, 0, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 0, 0), (2, 0, 0)) == 3
        and c2d4_cost((1, 0, 0), (1, 1, 0)) == 1
        and c2d4_cost((1, 1, 0), (1, 1, 1)) == 1
        and c2d4_cost((1, 1, 0), (1, 0, 0)) == 3
        and c2d4_cost((1, 1, 1), (2, 1, 1)) == 3
        and c2d4_cost((2, 2, 1), (3, 2, 1)) == 1
        and c2d4_cost((18, 18, 17), (18, 18, 18)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "c2d4(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
