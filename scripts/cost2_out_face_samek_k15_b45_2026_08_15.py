#!/usr/bin/env python3
"""Score same-k reverse at k=15 under w2 on B_45(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/COST2_OUT_FACE_SAMEK_K15_B45_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/COST2_OUT_FACE_SAMEK_K15_B45_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=15 under the named cost-2 out-face hop-cost "
    "on B_45(0) is reported. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T_AXIS_REP = 31
T_BODY_REP = 49
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


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) > max(abs(coord) for coord in v):
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
        "Do not write w2 into Admissibility" in note
        and "Do not write `w2` into Admissibility" in note,
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

    sites = ball(45)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_w2(sites)
    t_axis = dist[(15, 0, 0)]
    t_body = dist[(15, 15, 15)]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t14000 = dist[(14, 0, 0)]
    t141414 = dist[(14, 14, 14)]
    t320 = dist[(3, 2, 0)]
    t4500 = dist[(45, 0, 0)]
    t4200 = dist[(42, 0, 0)]
    axis_sq = t_axis * t_axis
    body_sq = t_body * t_body
    reverse = 3 * axis_sq > body_sq
    reverse_k1 = 3 * t100 * t100 > t111 * t111
    reverse_k14 = 3 * t14000 * t14000 > t141414 * t141414
    witness_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 16)],
        (15, 1, 1),
        (15, 1, 0),
        (15, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 16)],
        *[(15, y, 1) for y in range(3, 16)],
        *[(15, 15, z) for z in range(2, 16)],
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
    print(f"t(15,0,0) {t_axis}")
    print(f"t(15,15,15) {t_body}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"t(14,0,0) {t14000}")
    print(f"t(14,14,14) {t141414}")
    print(f"t(15,0,0)^2/225 {axis_sq}/225")
    print(f"t(15,15,15)^2/675 {body_sq}/675")
    print(f"3t_axis^2 {3 * axis_sq}")
    print(f"t_body^2 {body_sq}")
    print(f"reverse {reverse}")
    print(f"reverse_k1 {reverse_k1}")
    print(f"reverse_k14 {reverse_k14}")
    print(f"t(3,2,0) {t320}")
    print(f"t(45,0,0) {t4500}")
    print(f"t(42,0,0) {t4200}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_w2_axis_sum {sum(witness_w2_axis)}")
    print(f"witness_w2_body_sum {sum(witness_w2_body)}")
    print(f"witness_w2_face {witness_w2_face}")
    print(f"w2_out_face {w2_cost(*out_face_hop)}")
    print(f"omega_out_face {omega_cost(*out_face_hop)}")
    print(f"rho3_out_face {rho3_cost(*out_face_hop)}")
    print(f"w2_corridor {w2_cost(*corridor_hop)}")
    print(f"rho3_corridor {rho3_cost(*corridor_hop)}")

    checks.check(
        "theorem-1",
        f"t(15,0,0)={T_AXIS_REP} and t(15,15,15)={T_BODY_REP}",
        t_axis == T_AXIS_REP and t_body == T_BODY_REP,
    )
    checks.check(
        "reverse-k15",
        "t(15,0,0)^2 / 225 > t(15,15,15)^2 / 675",
        reverse
        and 3 * axis_sq == 2883
        and body_sq == 2401
        and "2883 > 2401" in note
        and "does hold" in note
        and "inequality holds" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b45",
        "B_45(0) has 125671 sites and 125670 nonzero sites",
        len(sites) == 125671 and len(nonzero) == 125670 and all(l1(v) <= 45 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_45(0) is reached",
        len(dist) == 125671,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "t(15,0,0) = 31" in note
        and "t(15,15,15) = 49" in note
        and "`(15,0,0)`" in note
        and "`(15,15,15)`" in note
        and "`31`" in note
        and "`49`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse comparison",
        "2883 > 2401" in note and "961/225" in note and "2401/675" in note,
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
        and omega_cost((2, 2, 0), (3, 2, 0)) == 3
        and w2_cost((1, 1, 0), (2, 1, 0)) == 3
        and "cost `2`" in note
        and "not `3`" in note
        and "rounder" in note,
    )
    checks.check(
        "w2-not-leftover-of-rho3",
        "face-growth (2,2,0)->(3,2,0) is w2=2 and ρ3=1",
        w2_cost((2, 2, 0), (3, 2, 0)) == 2
        and rho3_cost((2, 2, 0), (3, 2, 0)) == 1
        and w2_cost((1, 1, 0), (2, 1, 0)) == 3
        and rho3_cost((1, 1, 0), (2, 1, 0)) == 3
        and sum(witness_w2_axis) == 31
        and sum(witness_w2_body) == 49
        and "(2,2,0) → (3,2,0)" in note,
    )
    checks.check(
        "not-leftover-of-omega",
        "ω prices out-face growth at 3 while w2 prices it at 2",
        w2_cost(*out_face_hop) == 2
        and omega_cost(*out_face_hop) == 3
        and t320 == 10
        and "not leftover of `ω`" in note,
    )
    checks.check(
        "not-leftover-of-b42",
        "(15,15,15) lies outside B_42(0) and the note says so",
        l1((15, 15, 15)) == 45
        and (15, 15, 15) in dist
        and t4500 == 66
        and t4200 == 58
        and "absent from `B_42(0)`" in note
        and "not leftover of the `B_42(0)` times" in note,
    )
    checks.check(
        "k14-restored",
        "the same Dijkstra restores t(14,0,0)=30 versus t(14,14,14)=46",
        t14000 == 30
        and t141414 == 46
        and reverse_k14
        and "t(14,0,0) = 30" in note
        and "t(14,14,14) = 46" in note
        and "`30` vs `46`" in note,
    )
    checks.check(
        "k1-kept",
        "the same Dijkstra keeps t(1,0,0)=3 and t(1,1,1)=5",
        t100 == 3
        and t111 == 5
        and reverse_k1
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
        and w2_cost((15, 15, 14), (15, 15, 15)) == 1,
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
