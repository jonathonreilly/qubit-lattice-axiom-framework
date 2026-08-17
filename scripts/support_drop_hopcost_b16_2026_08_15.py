#!/usr/bin/env python3
"""Score the named support-drop hop-cost on B_16(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_HOPCOST_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_HOPCOST_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "On B_16(0), the named support-drop hop-cost is scored for "
    "same-k, doubled, and k=5 face reverse. "
    "Displayed, not adopted."
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


def dijkstra_nu(sites: list[tuple[int, int, int]]) -> dict[tuple[int, int, int], int]:
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
            nd = d + nu_cost(v, w)
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
        "ν is not written into Admissibility",
        "Do not write `ν` into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note,
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

    sites = ball(16)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_nu(sites)
    t400 = dist[(4, 0, 0)]
    t800 = dist[(8, 0, 0)]
    t444 = dist[(4, 4, 4)]
    t222 = dist[(2, 2, 2)]
    t1000 = dist[(10, 0, 0)]
    t550 = dist[(5, 5, 0)]
    t1600 = dist[(16, 0, 0)]
    k = 4
    t_k00 = dist[(k, 0, 0)]
    t_kkk = dist[(k, k, k)]
    diamond = 12 * t400 * t400 > 16 * t222 * t222
    doubled = 12 * t800 * t800 > 16 * t444 * t444
    same_k = (t400 * t400) / 16 > (t444 * t444) / 48
    face_k5 = (t1000 * t1000) / 100 > (t550 * t550) / 50

    print(f"n_sites {len(sites)}")
    print(f"t(4,0,0) {t400}")
    print(f"t(8,0,0) {t800}")
    print(f"t(4,4,4) {t444}")
    print(f"t(2,2,2) {t222}")
    print(f"t(10,0,0) {t1000}")
    print(f"t(5,5,0) {t550}")
    print(f"t(k,0,0) {t_k00}")
    print(f"t(k,k,k) {t_kkk}")
    print(f"t(16,0,0) {t1600}")
    print(f"12 t(4,0,0)^2 {12 * t400 * t400}")
    print(f"16 t(2,2,2)^2 {16 * t222 * t222}")
    print(f"12 t(8,0,0)^2 {12 * t800 * t800}")
    print(f"16 t(4,4,4)^2 {16 * t444 * t444}")
    print(f"t(4,0,0)^2/16 {t400 * t400}/16")
    print(f"t(4,4,4)^2/48 {t444 * t444}/48")
    print(f"t(10,0,0)^2/100 {t1000 * t1000}/100")
    print(f"t(5,5,0)^2/50 {t550 * t550}/50")
    print(f"diamond_reverse {diamond}")
    print(f"double_diamond_reverse {doubled}")
    print(f"same_k4_reverse {same_k}")
    print(f"face_k5_reverse {face_k5}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b16",
        "B_16(0) has 6017 sites and 6016 nonzero sites",
        len(sites) == 6017 and len(nonzero) == 6016 and all(l1(v) <= 16 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_16(0) is reached",
        len(dist) == 6017,
    )
    checks.check(
        "t-400",
        "t(4,0,0) = 10",
        t400 == 10,
    )
    checks.check(
        "t-800",
        "t(8,0,0) = 14",
        t800 == 14,
    )
    checks.check(
        "t-444",
        "t(4,4,4) = 14",
        t444 == 14,
    )
    checks.check(
        "t-222",
        "t(2,2,2) = 8",
        t222 == 8,
    )
    checks.check(
        "t-1000",
        "t(10,0,0) = 16",
        t1000 == 16,
    )
    checks.check(
        "t-550",
        "t(5,5,0) = 12",
        t550 == 12,
    )
    checks.check(
        "t-k4-axis-body",
        "t(k,0,0) and t(k,k,k) for k=4 are 10 and 14",
        k == 4 and t_k00 == 10 and t_kkk == 14,
    )
    checks.check(
        "diamond-reverse",
        "12 t(4,0,0)^2 > 16 t(2,2,2)^2",
        diamond and 12 * t400 * t400 == 1200 and 16 * t222 * t222 == 1024,
    )
    checks.check(
        "double-diamond-not-reverse",
        "12 t(8,0,0)^2 > 16 t(4,4,4)^2 fails",
        (not doubled) and 12 * t800 * t800 == 2352 and 16 * t444 * t444 == 3136,
    )
    checks.check(
        "same-k4-reverse",
        "t(4,0,0)^2/16 > t(4,4,4)^2/48",
        same_k and 3 * t400 * t400 == 300 and t444 * t444 == 196,
    )
    checks.check(
        "face-k5-not-reverse",
        "t(10,0,0)^2/100 > t(5,5,0)^2/50 fails",
        (not face_k5)
        and 50 * t1000 * t1000 == 12800
        and 100 * t550 * t550 == 14400,
    )
    checks.check(
        "note-records-times",
        "note records the computed arrivals",
        "t(4,0,0) = 10" in note
        and "t(8,0,0) = 14" in note
        and "t(4,4,4) = 14" in note
        and "t(2,2,2) = 8" in note
        and "t(10,0,0) = 16" in note
        and "t(5,5,0) = 12" in note
        and "t(k,0,0) = 10" in note
        and "t(k,k,k) = 14" in note,
    )
    checks.check(
        "note-records-comparisons",
        "note records all four product pairs",
        "1200" in note
        and "1024" in note
        and "2352" in note
        and "3136" in note
        and "100/16" in note
        and "196/48" in note
        and "256/100" in note
        and "144/50" in note
        and "12800" in note
        and "14400" in note,
    )
    checks.check(
        "not-leftover-of-b12",
        "the B_16(0) table is not leftover of the B_12(0) times",
        t1600 == 24
        and t1600 != 20
        and l1((16, 0, 0)) == 16
        and (16, 0, 0) in dist
        and "not leftover of the `B_12(0)` times" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (1, 0, 0)) == 3
        and nu_cost((1, 0, 0), (2, 0, 0)) == 3
        and nu_cost((1, 0, 0), (1, 1, 0)) == 1
        and nu_cost((1, 1, 0), (1, 1, 1)) == 1
        and nu_cost((1, 1, 0), (1, 0, 0)) == 3,
    )
    checks.check(
        "axis-boundary-last-step",
        "(16,0,0) has only the axis in-ball neighbor (15,0,0)",
        {(16 + dx, 0 + dy, 0 + dz) for dx, dy, dz in NEIGH if l1((16 + dx, dy, dz)) <= 16}
        == {(15, 0, 0)}
        and t1600 == dist[(15, 0, 0)] + 3,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
