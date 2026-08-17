#!/usr/bin/env python3
"""Named (0,1,1) hop-cost arrival times on B_12(0).

One Dijkstra from the origin. Displayed, not adopted. No axiom edit,
no cache write, no L1 hop-cost attachment.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = "CLAUSE_011_REVERSE_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_REVERSE_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BALL_RADIUS = 12
AXIS = ((4, 0, 0), (8, 0, 0), (12, 0, 0))
DIAG = ((2, 2, 2), (4, 4, 4))
TARGETS = AXIS + DIAG
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def nn_radius(site: tuple[int, int, int]) -> int:
    return abs(site[0]) + abs(site[1]) + abs(site[2])


def in_ball(site: tuple[int, int, int]) -> bool:
    return nn_radius(site) <= BALL_RADIUS


def support_size(site: tuple[int, int, int]) -> int:
    return int(site[0] != 0) + int(site[1] != 0) + int(site[2] != 0)


def hop_cost(src: tuple[int, int, int], dst: tuple[int, int, int]) -> int:
    """Rule (0,1,1): cost 3 iff both weights 1 or support drop, else 1."""
    src_support = support_size(src)
    dst_support = support_size(dst)
    both_weights_one = src_support == 1 and dst_support == 1
    support_drop = dst_support < src_support
    if both_weights_one or support_drop:
        return 3
    return 1


def ball_sites() -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-BALL_RADIUS, BALL_RADIUS + 1):
        for y in range(-BALL_RADIUS, BALL_RADIUS + 1):
            remain = BALL_RADIUS - abs(x) - abs(y)
            if remain < 0:
                continue
            for z in range(-remain, remain + 1):
                sites.append((x, y, z))
    return sites


def neighbors(site: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    x, y, z = site
    out: list[tuple[int, int, int]] = []
    for dx, dy, dz in NEIGHBOR_STEPS:
        nxt = (x + dx, y + dy, z + dz)
        if in_ball(nxt):
            out.append(nxt)
    return out


def dijkstra_from_origin(
    sites: list[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
    origin = (0, 0, 0)
    dist = {origin: 0}
    heap = [(0, origin)]
    while heap:
        cost_here, site = heapq.heappop(heap)
        if cost_here != dist[site]:
            continue
        for nxt in neighbors(site):
            cand = cost_here + hop_cost(site, nxt)
            if cand < dist.get(nxt, 10**9):
                dist[nxt] = cand
                heapq.heappush(heap, (cand, nxt))
    if len(dist) != len(sites):
        raise RuntimeError("Dijkstra did not reach every site of B_12(0)")
    return dist


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


def audit_paths_are_static_literals() -> bool:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            names = [t.id for t in node.targets if isinstance(t, ast.Name)]
            if "AUDIT_INPUT_PATHS" in names:
                value = node.value
                if not isinstance(value, ast.Tuple):
                    return False
                return all(
                    isinstance(elt, ast.Constant) and isinstance(elt.value, str)
                    for elt in value.elts
                )
    return False


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")

    print(
        "external_scientific_inputs: none; hop-costs are the named (0,1,1) "
        "rule on the finite 12-hop neighborhood B_12(0)"
    )
    print(
        "package_local_integrity_reads: the note and current minimal axiom "
        "are read; no cache or governance surface is written"
    )
    print(
        "negative_scope: the named rule is displayed, not adopted; it is "
        "not written into Admissibility and is not attached as an L1 hop-cost"
    )

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static literal pair and both files exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_REVERSE_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals()
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites()
    checks.check(
        "ball-b12-only",
        "B_12(0) is the 12-hop neighborhood of the origin and contains every named target",
        len(sites) == 2625
        and all(in_ball(site) for site in TARGETS)
        and (12, 0, 0) in sites
        and (4, 4, 4) in sites
        and (13, 0, 0) not in set(sites),
    )

    checks.check(
        "clause-011-local",
        "seed-exit costs 1; axis 1-skeleton and support-drop cost 3; else 1",
        hop_cost((0, 0, 0), (1, 0, 0)) == 1
        and hop_cost((1, 0, 0), (2, 0, 0)) == 3
        and hop_cost((1, 1, 0), (1, 0, 0)) == 3
        and hop_cost((1, 1, 0), (2, 1, 0)) == 1
        and hop_cost((1, 0, 0), (1, 1, 0)) == 1,
    )

    distances = dijkstra_from_origin(sites)
    t400 = distances[(4, 0, 0)]
    t800 = distances[(8, 0, 0)]
    t1200 = distances[(12, 0, 0)]
    t222 = distances[(2, 2, 2)]
    t444 = distances[(4, 4, 4)]
    left_small = 12 * t400 * t400
    right_small = 16 * t222 * t222
    left_double = 12 * t800 * t800
    right_double = 16 * t444 * t444
    reverse_small = left_small > right_small
    reverse_double = left_double > right_double

    print(f"t(4,0,0)={t400}")
    print(f"t(8,0,0)={t800}")
    print(f"t(12,0,0)={t1200}")
    print(f"t(2,2,2)={t222}")
    print(f"t(4,4,4)={t444}")
    print(f"12 t(4,0,0)^2={left_small} 16 t(2,2,2)^2={right_small} reverse={reverse_small}")
    print(f"12 t(8,0,0)^2={left_double} 16 t(4,4,4)^2={right_double} reverse={reverse_double}")
    print("dijkstra_count=1")

    checks.check(
        "theorem-1-times",
        "the five named arrival times are the Dijkstra values 8,12,18,6,12",
        (t400, t800, t1200, t222, t444) == (8, 12, 18, 6, 12),
    )
    checks.check(
        "theorem-2-small-pair",
        "12 t(4,0,0)^2 > 16 t(2,2,2)^2 holds (768 > 576)",
        reverse_small and left_small == 768 and right_small == 576,
    )
    checks.check(
        "theorem-2-doubled-pair",
        "12 t(8,0,0)^2 > 16 t(4,4,4)^2 fails (1728 > 2304 is false)",
        (not reverse_double) and left_double == 1728 and right_double == 2304,
    )
    checks.check(
        "scale-survival",
        "body-diagonal reverse does not survive the doubled pair on B_12(0)",
        reverse_small and not reverse_double,
    )
    checks.check(
        "one-dijkstra",
        "a single origin Dijkstra assigned a finite time to every ball site",
        len(distances) == len(sites) and all(distances[site] >= 0 for site in sites),
    )
    checks.check(
        "note-reports-times",
        "the note reports the five computed times and both displayed comparisons",
        "t(4,0,0)=8" in note
        and "t(8,0,0)=12" in note
        and "t(12,0,0)=18" in note
        and "t(2,2,2)=6" in note
        and "t(4,4,4)=12" in note
        and "768 > 576" in note
        and "1728 > 2304" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "the note displays the (0,1,1) scores and does not adopt them",
        "Displayed, not adopted" in note
        and "do not write (0,1,1) into Admissibility" in note
        and "Do not attach L1" in note,
    )
    checks.check(
        "admissibility-unedited",
        "the current axiom memo still names Admissibility and does not contain the hop-cost rule",
        "Admissibility" in axiom
        and "Lattice" in axiom
        and "Qubit" in axiom
        and "Record" in axiom
        and "both weights 1 or support drop" not in axiom
        and "(0,1,1)" not in axiom,
    )
    checks.check(
        "claim-scope",
        "the note states the required claim_scope",
        "Body-diagonal reverse under the named (0,1,1) hop-cost on B_12(0) is reported"
        in note,
    )
    checks.check(
        "forbidden-tokens",
        "the note avoids the forbidden tokens",
        "G_N" not in note
        and "1/r" not in note
        and "1/r^2" not in note
        and "Lattice-named" not in note
        and "not a TOE" not in note,
    )
    checks.check(
        "uniqueness-not-required",
        "the note does not claim uniqueness of the named rule",
        "Uniqueness is not required" in note
        and "unique hop-cost" not in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
