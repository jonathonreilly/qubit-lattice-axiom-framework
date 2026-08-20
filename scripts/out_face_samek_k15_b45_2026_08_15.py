#!/usr/bin/env python3
"""Score same-k reverse at k=15 under ω on B_45(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/OUT_FACE_SAMEK_K15_B45_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/OUT_FACE_SAMEK_K15_B45_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=15 under the named out-face hop-cost "
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


def unit_count(v: tuple[int, int, int]) -> int:
    return int(abs(v[0]) == 1) + int(abs(v[1]) == 1) + int(abs(v[2]) == 1)


def least_nonzero_abs(v: tuple[int, int, int]) -> int | None:
    nonzero = [abs(c) for c in v if c != 0]
    if not nonzero:
        return None
    return min(nonzero)


def max_abs(v: tuple[int, int, int]) -> int:
    return max(abs(v[0]), abs(v[1]), abs(v[2]))


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
    if support_size(v) == 3 and support_size(w) == 3 and unit_count(w) == 2:
        return 3
    return 1


def omega_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if rho3_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2 and max_abs(w) > max_abs(v):
        return 3
    return 1


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
        "Do not write `ω` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "uniqueness-not-claimed",
        "uniqueness among hop-costs is not claimed",
        "Uniqueness is not claimed" in note or "no uniqueness" in note.lower(),
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

    sites = ball(45)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_omega(sites)
    t15000 = dist[(15, 0, 0)]
    t151515 = dist[(15, 15, 15)]
    t4500 = dist[(45, 0, 0)]
    t4200 = dist[(42, 0, 0)]
    t320 = dist[(3, 2, 0)]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t14000 = dist[(14, 0, 0)]
    t141414 = dist[(14, 14, 14)]
    reverse = 3 * t15000 * t15000 > t151515 * t151515
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
    witness_omega_axis = [omega_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])]
    witness_omega_body = [omega_cost(a, b) for a, b in zip(witness_body, witness_body[1:])]
    out_face_hop = ((2, 2, 0), (3, 2, 0))
    corridor_hop = ((1, 1, 0), (2, 1, 0))
    ridge_hop = ((1, 1, 1), (2, 1, 1))
    interior_body_hop = ((15, 15, 1), (15, 15, 2))
    print(f"n_sites {len(sites)}")
    print(f"t(15,0,0) {t15000}")
    print(f"t(15,15,15) {t151515}")
    print(f"t(15,0,0)^2/225 {t15000 * t15000}/225")
    print(f"t(15,15,15)^2/675 {t151515 * t151515}/675")
    print(f"3t_axis^2 {3 * t15000 * t15000}")
    print(f"t_body^2 {t151515 * t151515}")
    print(f"reverse {reverse}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"reverse_k1 {reverse_k1}")
    print(f"t(14,0,0) {t14000}")
    print(f"t(14,14,14) {t141414}")
    print(f"reverse_k14 {reverse_k14}")
    print(f"t(45,0,0) {t4500}")
    print(f"t(42,0,0) {t4200}")
    print(f"t(3,2,0) {t320}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_omega_axis {witness_omega_axis}")
    print(f"witness_omega_axis_sum {sum(witness_omega_axis)}")
    print(f"witness_omega_body_sum {sum(witness_omega_body)}")
    print(f"omega_out_face {omega_cost(*out_face_hop)}")
    print(f"rho3_out_face {rho3_cost(*out_face_hop)}")
    print(f"omega_corridor {omega_cost(*corridor_hop)}")
    print(f"rho3_corridor {rho3_cost(*corridor_hop)}")
    print(f"omega_ridge {omega_cost(*ridge_hop)}")
    print(f"rho3_ridge {rho3_cost(*ridge_hop)}")
    print(f"omega_interior_body {omega_cost(*interior_body_hop)}")
    print(f"rho3_interior_body {rho3_cost(*interior_body_hop)}")

    checks.check(
        "t-15000-151515",
        f"t(15,0,0)={T_AXIS_REP} and t(15,15,15)={T_BODY_REP}",
        t15000 == T_AXIS_REP and t151515 == T_BODY_REP,
    )
    checks.check(
        "reverse-k15",
        "t(15,0,0)^2/225 > t(15,15,15)^2/675 holds",
        reverse
        and 3 * t15000 * t15000 == 2883
        and t151515 * t151515 == 2401
        and "2883 > 2401" in note
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
        "`31`" in note
        and "`49`" in note
        and "`(15,0,0)`" in note
        and "`(15,15,15)`" in note
        and "t(15,0,0) = 31" in note
        and "t(15,15,15) = 49" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the integer reverse products",
        "2883 > 2401" in note and "961/225" in note and "2401/675" in note,
    )
    checks.check(
        "not-leftover-of-rho3",
        "ω prices the out-face hop at 3 while ρ3 prices it at 1",
        omega_cost(*out_face_hop) == 3
        and rho3_cost(*out_face_hop) == 1
        and omega_cost(*corridor_hop) == 3
        and rho3_cost(*corridor_hop) == 3
        and sum(witness_omega_axis) == 31
        and sum(witness_omega_body) == 49
        and t15000 == 31
        and t151515 == 49
        and t320 == 11
        and "cannot price the out-face" in note
        and "`t(3,2,0) = 11`" in note,
    )
    checks.check(
        "not-leftover-of-b42",
        "(15,15,15) lies outside B_42(0) and the note says so",
        l1((15, 15, 15)) == 45
        and (15, 15, 15) in dist
        and t4500 == 67
        and t4200 == 58
        and "absent from `B_42(0)`" in note
        and "not leftover of the `B_42(0)` times" in note,
    )
    checks.check(
        "keeps-k1-and-restores-k14",
        "the same Dijkstra keeps k=1 reverse and restores k=14 as 30 vs 46",
        t100 == 3
        and t111 == 5
        and reverse_k1
        and t14000 == 30
        and t141414 == 46
        and reverse_k14
        and "keeps reverse at `k=1`" in note
        and "`30` versus `46`" in note,
    )
    checks.check(
        "seed-and-out-face-clauses",
        "seed-exit, both-weights-1, support-drop, corridor-slide, ridge-slide, and out-face grow cost 3; other hops cost 1",
        omega_cost((0, 0, 0), (1, 0, 0)) == 3
        and omega_cost((1, 0, 0), (2, 0, 0)) == 3
        and omega_cost((1, 1, 0), (1, 0, 0)) == 3
        and omega_cost((1, 1, 0), (2, 1, 0)) == 3
        and omega_cost((1, 1, 1), (2, 1, 1)) == 3
        and omega_cost((2, 2, 0), (3, 2, 0)) == 3
        and omega_cost((1, 0, 0), (1, 1, 0)) == 1
        and omega_cost((1, 1, 0), (1, 1, 1)) == 1
        and omega_cost((2, 2, 1), (3, 2, 1)) == 1
        and omega_cost(*interior_body_hop) == 1
        and omega_cost((15, 15, 14), (15, 15, 15)) == 1
        and omega_cost((15, 2, 0), (15, 3, 0)) == 1,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ω(v→w)" not in axiom
        and "ρ3(v→w)" not in axiom
        and "μ(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
