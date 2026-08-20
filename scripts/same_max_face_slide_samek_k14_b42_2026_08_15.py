#!/usr/bin/env python3
"""Score same-k reverse at k=14 under ψ on B_42(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SAME_MAX_FACE_SLIDE_SAMEK_K14_B42_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SAME_MAX_FACE_SLIDE_SAMEK_K14_B42_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Same-k reverse at k=14 under the named same-max face-slide hop-cost "
    "on B_42(0) is reported. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
T_AXIS_REP = 30
T_BODY_REP = 46
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


def psi_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    if omega_cost(v, w) == 3:
        return 3
    if support_size(v) == 2 and support_size(w) == 2:
        if max(abs(coord) for coord in w) == max(abs(coord) for coord in v):
            return 3
    return 1


def ball(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def dijkstra_psi(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + psi_cost(v, w)
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
        "ψ is not written into Admissibility",
        "Do not write `ψ` into Admissibility" in note,
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

    sites = ball(42)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_psi(sites)
    t14000 = dist[(14, 0, 0)]
    t141414 = dist[(14, 14, 14)]
    t100 = dist[(1, 0, 0)]
    t111 = dist[(1, 1, 1)]
    t220 = dist[(2, 2, 0)]
    reverse = 3 * t14000 * t14000 > t141414 * t141414
    witness_axis = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 15)],
        (14, 1, 1),
        (14, 1, 0),
        (14, 0, 0),
    )
    witness_body = (
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 1),
        *[(x, 2, 1) for x in range(3, 15)],
        *[(14, y, 1) for y in range(3, 15)],
        *[(14, 14, z) for z in range(2, 15)],
    )
    witness_psi_axis = [psi_cost(a, b) for a, b in zip(witness_axis, witness_axis[1:])]
    witness_psi_body = [psi_cost(a, b) for a, b in zip(witness_body, witness_body[1:])]
    same_max_hop = ((2, 1, 0), (2, 2, 0))
    box_growth_hop = ((1, 1, 0), (2, 1, 0))
    interior_body_hop = ((14, 14, 1), (14, 14, 2))
    print(f"n_sites {len(sites)}")
    print(f"t(14,0,0) {t14000}")
    print(f"t(14,14,14) {t141414}")
    print(f"t(14,0,0)^2/196 {t14000 * t14000}/196")
    print(f"t(14,14,14)^2/588 {t141414 * t141414}/588")
    print(f"3t_axis^2 {3 * t14000 * t14000}")
    print(f"t_body^2 {t141414 * t141414}")
    print(f"reverse {reverse}")
    print(f"t(1,0,0) {t100}")
    print(f"t(1,1,1) {t111}")
    print(f"t(2,2,0) {t220}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print(f"witness_psi_axis {witness_psi_axis}")
    print(f"witness_psi_axis_sum {sum(witness_psi_axis)}")
    print(f"witness_psi_body_sum {sum(witness_psi_body)}")
    print(f"psi_same_max {psi_cost(*same_max_hop)}")
    print(f"omega_same_max {omega_cost(*same_max_hop)}")
    print(f"psi_box_growth {psi_cost(*box_growth_hop)}")
    print(f"omega_box_growth {omega_cost(*box_growth_hop)}")

    checks.check(
        "theorem-1",
        f"t(14,0,0)={T_AXIS_REP} and t(14,14,14)={T_BODY_REP}",
        t14000 == T_AXIS_REP and t141414 == T_BODY_REP,
    )
    checks.check(
        "reverse-k14",
        "t(14,0,0)^2 / 196 > t(14,14,14)^2 / 588",
        reverse
        and 3 * t14000 * t14000 == 2700
        and t141414 * t141414 == 2116
        and "2700 > 2116" in note,
    )
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b42",
        "B_42(0) has 102425 sites and 102424 nonzero sites",
        len(sites) == 102425 and len(nonzero) == 102424 and all(l1(v) <= 42 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_42(0) is reached",
        len(dist) == 102425,
    )
    checks.check(
        "note-records-times",
        "note records the two computed arrivals",
        "`(14,0,0)`" in note
        and "`(14,14,14)`" in note
        and "`30`" in note
        and "`46`" in note,
    )
    checks.check(
        "note-records-reverse-product",
        "note records the integer reverse comparison",
        "2700 > 2116" in note,
    )
    checks.check(
        "same-max-face-slide-hop",
        "the named same-max hop (2,1,0)->(2,2,0) has ψ=3 and ω=1",
        psi_cost(*same_max_hop) == 3
        and omega_cost(*same_max_hop) == 1
        and support_size((2, 1, 0)) == 2
        and support_size((2, 2, 0)) == 2
        and max(abs(c) for c in (2, 2, 0)) == max(abs(c) for c in (2, 1, 0))
        and "(2,1,0) → (2,2,0)" in note
        and t220 == 10
        and "`t(2,2,0) = 10`" in note,
    )
    checks.check(
        "psi-not-leftover-of-omega",
        "same-max slide is new over ω; box-growth remains ψ=3",
        psi_cost(*same_max_hop) == 3
        and omega_cost(*same_max_hop) == 1
        and omega_cost(*box_growth_hop) == 3
        and psi_cost(*box_growth_hop) == 3
        and "(1,1,0) → (2,1,0)" in note
        and sum(witness_psi_axis) == 30
        and sum(witness_psi_body) == 46,
    )
    checks.check(
        "k14-geodesic-costs",
        "the k=14 axis and body witnesses use no same-max 2→2 hop",
        all(psi_cost(a, b) in (1, 3) for a, b in zip(witness_axis, witness_axis[1:]))
        and all(
            not (
                support_size(a) == 2
                and support_size(b) == 2
                and max(abs(c) for c in b) == max(abs(c) for c in a)
            )
            for a, b in zip(witness_axis, witness_axis[1:])
        )
        and all(
            not (
                support_size(a) == 2
                and support_size(b) == 2
                and max(abs(c) for c in b) == max(abs(c) for c in a)
            )
            for a, b in zip(witness_body, witness_body[1:])
        )
        and t100 == 3
        and t111 == 5
        and psi_cost(*interior_body_hop) == 1,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        psi_cost((0, 0, 0), (1, 0, 0)) == 3
        and psi_cost((1, 0, 0), (2, 0, 0)) == 3
        and psi_cost((1, 0, 0), (1, 1, 0)) == 1
        and psi_cost((1, 1, 0), (1, 1, 1)) == 1
        and psi_cost((1, 1, 0), (1, 0, 0)) == 3
        and l1((14, 14, 14)) == 42
        and "absent from `B_39(0)`" in note,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ψ(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
