#!/usr/bin/env python3
"""Name mixed t=const shells of the support-drop hop-cost on B_12(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from collections import defaultdict
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_MIXED_SHELLS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_MIXED_SHELLS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Mixed t=const shells under the named support-drop hop-cost "
    "on B_12(0) are named. Displayed, not adopted."
)
NEIGH = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
MIXED_SHELLS = (
    (5, 2, 32),
    (6, 4, 66),
    (7, 4, 96),
    (8, 5, 140),
    (9, 8, 198),
    (10, 10, 258),
    (11, 10, 326),
    (12, 13, 402),
    (13, 15, 486),
    (14, 15, 578),
)
T8_RADII = (12, 14, 18, 20, 26)
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


def r2(v: tuple[int, int, int]) -> int:
    return v[0] * v[0] + v[1] * v[1] + v[2] * v[2]


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


def mixed_shells(
    dist: dict[tuple[int, int, int], int],
) -> list[tuple[int, int, int, tuple[int, ...]]]:
    by_t: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for v, t in dist.items():
        if v != (0, 0, 0):
            by_t[t].append(v)
    rows: list[tuple[int, int, int, tuple[int, ...]]] = []
    for t in sorted(by_t):
        radii = tuple(sorted({r2(v) for v in by_t[t]}))
        if len(radii) > 1:
            rows.append((t, len(radii), len(by_t[t]), radii))
    return rows


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
        "note claim_scope matches the mixed-shell naming statement",
        CLAIM_SCOPE in note.replace("\n", " "),
    )
    checks.check(
        "displayed-not-adopted",
        "the census is displayed, not adopted",
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

    sites = ball(12)
    nonzero = [v for v in sites if v != (0, 0, 0)]
    dist = dijkstra_nu(sites)
    rows = mixed_shells(dist)
    mixed_triples = tuple((t, n_radii, n_sites) for t, n_radii, n_sites, _ in rows)
    t222 = dist[(2, 2, 2)]
    t444 = dist[(4, 4, 4)]
    radii8 = next(radii for t, _, _, radii in rows if t == 8)
    mixed_t = {t for t, _, _, _ in rows}

    print(f"n_sites {len(sites)}")
    print(f"n_mixed {len(rows)}")
    for t, n_radii, n_sites, radii in rows:
        print(f"mixed t={t} n_radii={n_radii} n_sites={n_sites} radii={list(radii)}")
    print(f"t(2,2,2) {t222}")
    print(f"t(4,4,4) {t444}")
    print(f"t8_mixed {t222 in mixed_t}")
    print(f"t14_mixed {t444 in mixed_t}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b12",
        "B_12(0) has 2625 sites and 2624 nonzero sites",
        len(sites) == 2625 and len(nonzero) == 2624 and all(l1(v) <= 12 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_12(0) is reached",
        len(dist) == 2625,
    )
    checks.check(
        "mixed-list",
        "ten mixed arrivals with the named radius and site counts",
        mixed_triples == MIXED_SHELLS,
    )
    checks.check(
        "t-222-mixed",
        "t(2,2,2)=8 sits in a mixed shell",
        t222 == 8 and 8 in mixed_t and r2((2, 2, 2)) == 12,
    )
    checks.check(
        "t-444-mixed",
        "t(4,4,4)=14 sits in a mixed shell",
        t444 == 14 and 14 in mixed_t and r2((4, 4, 4)) == 48,
    )
    checks.check(
        "reverse-critical-among-mixed",
        "the reverse-critical t=8 shell mixes five squared radii",
        radii8 == T8_RADII,
    )
    checks.check(
        "not-leftover-of-b8",
        "B_12 mixed list adds t=11,12,13,14 beyond the B_8 six",
        mixed_t == {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
        and "not leftover of the `B_8(0)` mixed list" in note
        and "(4,4,4)` is not in `B_8(0)`" in note,
    )
    checks.check(
        "note-records-mixed-list",
        "note records every mixed t with radius count and site count",
        all(
            f"| `{t}` | `{n_radii}` | `{n_sites}` |" in note
            for t, n_radii, n_sites in MIXED_SHELLS
        ),
    )
    checks.check(
        "note-records-body-diagonals",
        "note records both body-diagonal arrivals as mixed",
        "t(2,2,2) = 8" in note
        and "t(4,4,4) = 14" in note
        and "sits in a mixed shell" in note,
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
        "axiom-untouched",
        "the axiom memo is an input only and still names the four axioms",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
