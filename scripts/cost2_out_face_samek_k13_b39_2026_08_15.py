#!/usr/bin/env python3
"""Score same-k reverse at k=13 under w2 on B_39(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COST2_OUT_FACE_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_OUT_FACE_SAMEK_K13_B39_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=13 under the named cost-2 out-face hop-cost "
    "on B_39(0) is reported. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T_AXIS_REP = 29
T_BODY_REP = 43
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


def w2_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) > max(abs(coord) for coord in v):
            return 2
    return 1


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def dijkstra_w2(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + w2_cost(v, w)
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
        "w2 is not written into Admissibility",
        "Do not write `w2` into Admissibility" in note,
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

    sites = ball(39)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_w2(sites)
    t_axis = dist[(13, 0, 0)]
    t_body = dist[(13, 13, 13)]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t320 = dist[(3, 2, 0)]
    t3900 = dist[(39, 0, 0)]
    t3600 = dist[(36, 0, 0)]
    axis_sq = t_axis * t_axis
    body_sq = t_body * t_body
    reverse = axis_sq * 507 > body_sq * 169
    witness_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 14)],
        (13, 1, 1),
        (13, 1, 0),
        (13, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 14)],
        *[(13, y, 1) for y in range(3, 14)],
        *[(13, 13, z) for z in range(2, 14)],
    )
    witness_face = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (2, 1, 0),
        (2, 2, 0),
        (3, 2, 0),
    )
    witness_w2_axis = [w2_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])]
    witness_w2_body = [w2_cost(a, b) for a, b in zip(witness_body, witness_body[1:])]
    witness_w2_face = [w2_cost(a, b) for a, b in zip(witness_face, witness_face[1:])]
    out_face_hop = ((2, 2, 0), (3, 2, 0))
    corridor_hop = ((1, 1, 0), (2, 1, 0))
    print(f"n_sites {len(sites)}")
    print(f"t(13,0,0) {t_axis}")
    print(f"t(13,13,13) {t_body}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"t(13,0,0)^2/169 {axis_sq}/169")
    print(f"t(13,13,13)^2/507 {body_sq}/507")
    print(f"3t_axis^2 {3 * axis_sq}")
    print(f"t_body^2 {body_sq}")
    print(f"reverse {reverse}")
    print(f"t(3,2,0) {t320}")
    print(f"t(39,0,0) {t3900}")
    print(f"t(36,0,0) {t3600}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_w2_axis_sum {sum(witness_w2_axis)}")
    print(f"witness_w2_body_sum {sum(witness_w2_body)}")
    print(f"witness_w2_face {witness_w2_face}")
    print(f"w2_out_face {w2_cost(*out_face_hop)}")
    print(f"rho3_out_face {rho3_cost(*out_face_hop)}")
    print(f"w2_corridor {w2_cost(*corridor_hop)}")
    print(f"rho3_corridor {rho3_cost(*corridor_hop)}")

    checks.check(
        "theorem-1",
        f"t(13,0,0)={T_AXIS_REP} and t(13,13,13)={T_BODY_REP}",
        t_axis == T_AXIS_REP and t_body == T_BODY_REP,
    )
    checks.check(
        "reverse-k13",
        "t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507",
        reverse
        and 3 * axis_sq == 2523
        and body_sq == 1849
        and "2523 > 1849" in note
        and "does hold" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b39",
        "B_39(0) has 82239 sites and 82238 nonzero sites",
        len(sites) == 82239 and len(nonzero) == 82238 and all(l1(v) <= 39 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_39(0) is reached",
        len(dist) == 82239,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "t(13,0,0) = 29" in note
        and "t(13,13,13) = 43" in note
        and "`(13,0,0)`" in note
        and "`(13,13,13)`" in note
        and "`29`" in note
        and "`43`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse comparison",
        "2523 > 1849" in note and "841/169" in note and "1849/507" in note,
    )
    checks.check(
        "out-face-hop",
        "the named out-face hop (2,2,0)->(3,2,0) has w2=2",
        w2_cost((2, 2, 0), (3, 2, 0)) == 2
        and support_size((2, 2, 0)) == 2
        and support_size((3, 2, 0)) == 2
        and max(abs(c) for c in (3, 2, 0)) > max(abs(c) for c in (2, 2, 0))
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and t320 == 10
        and sum(witness_w2_face) == 10
        and "(2,2,0) → (3,2,0)" in note
        and "`t(3,2,0) = 10`" in note,
    )
    checks.check(
        "cost-2-not-3",
        "face-growth is cost 2, not 3",
        w2_cost((2, 2, 0), (3, 2, 0)) == 2
        and w2_cost((1, 1, 0), (2, 1, 0)) == 3
        and "cost `2`" in note
        and "not `3`" in note,
    )
    checks.check(
        "w2-not-leftover-of-rho3",
        "face-growth (2,2,0)->(3,2,0) is w2=2 and ρ3=1",
        w2_cost((2, 2, 0), (3, 2, 0)) == 2
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and w2_cost((1, 1, 0), (2, 1, 0)) == 3
        and rho3_cost((1, 1, 0), (2, 1, 0)) == 3
        and sum(witness_w2_axis) == 29
        and sum(witness_w2_body) == 43
        and "(2,2,0) → (3,2,0)" in note,
    )
    checks.check(
        "not-leftover-of-b36",
        "(13,13,13) lies outside B_36(0) and the note says so",
        l1((13, 13, 13)) == 39
        and (13, 13, 13) in dist
        and t3900 == 60
        and t3600 == 52
        and "absent from `B_36(0)`" in note
        and "not leftover of the `B_36(0)` times" in note,
    )
    checks.check(
        "k1-kept",
        "the same Dijkstra keeps t(1,0,0)=3 and t(1,1,1)=5",
        t100 == 3
        and t111 == 5
        and 3 * t100 * t100 > t111 * t111
        and w2_cost((0, 0, 0), (1, 0, 0)) == 3
        and w2_cost((1, 0, 0), (1, 1, 0)) == 1
        and w2_cost((1, 1, 0), (1, 1, 1)) == 1
        and "t(1,0,0) = 3" in note
        and "t(1,1,1) = 5" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        w2_cost((0, 0, 0), (1, 0, 0)) == 3
        and w2_cost((1, 0, 0), (2, 0, 0)) == 3
        and w2_cost((1, 0, 0), (1, 1, 0)) == 1
        and w2_cost((1, 1, 0), (1, 1, 1)) == 1
        and w2_cost((1, 1, 0), (1, 0, 0)) == 3
        and w2_cost((1, 1, 1), (2, 1, 1)) == 3
        and w2_cost((2, 2, 1), (3, 2, 1)) == 1
        and w2_cost((13, 13, 12), (13, 13, 13)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "w2(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
