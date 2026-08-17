#!/usr/bin/env python3
"""Named (0,1,1) same-k axis/body-diagonal ratios on B_16(0).

One Dijkstra from the origin. Displayed, not adopted. No axiom edit,
no cache write, no L1 hop-cost attachment.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = "CLAUSE_011_SCALE_RATIOS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_SCALE_RATIOS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BALL_RADIUS = 16
SCALES = (1, 2, 3, 4, 5)
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN_PARTS = (
    ("G_", "N"),
    ("1/", "r"),
    ("1/", "r^2"),
    ("Lattice-", "named"),
    ("not a ", "TOE"),
)
DIJKSTRA_CALLS = 0


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
    global DIJKSTRA_CALLS
    DIJKSTRA_CALLS += 1
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
        raise RuntimeError("Dijkstra did not reach every site of B_16(0)")
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
        "rule on the finite 16-hop neighborhood B_16(0)"
    )
    print(
        "package_local_integrity_reads: the note and current minimal axiom "
        "are read; no cache or governance surface is written"
    )
    print(
        "negative_scope: the named rule is displayed, not adopted; it is "
        "not written into Admissibility and is not attached as an L1 hop-cost"
    )
    print("cache_write: false")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static literal pair and both files exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_SCALE_RATIOS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals()
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites()
    targets = tuple((k, 0, 0) for k in SCALES) + tuple((k, k, k) for k in SCALES)
    checks.check(
        "ball-b16-only",
        "B_16(0) is the 16-hop neighborhood of the origin and contains every named target",
        len(sites) == 6017
        and all(in_ball(site) for site in targets)
        and (5, 5, 5) in sites
        and (16, 0, 0) in set(sites)
        and (17, 0, 0) not in set(sites)
        and nn_radius((5, 5, 5)) == 15
        and nn_radius((4, 4, 4)) == 12,
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
    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print("dijkstra_count=1")

    rows: list[tuple[int, int, int, int, int, bool]] = []
    for k in SCALES:
        t_axis = distances[(k, 0, 0)]
        t_body = distances[(k, k, k)]
        left = 3 * t_axis * t_axis
        right = t_body * t_body
        reverse = left > right
        rows.append((k, t_axis, t_body, left, right, reverse))
        print(
            f"k {k} t({k},0,0)={t_axis} t({k},{k},{k})={t_body} "
            f"3t_axis^2={left} t_body^2={right} reverse={reverse}"
        )

    computed = {k: (t_axis, t_body) for k, t_axis, t_body, _l, _r, _rev in rows}
    reverse_by_k = {k: rev for k, _a, _b, _l, _r, rev in rows}

    checks.check(
        "theorem-1-times",
        "the ten same-k arrival times are the Dijkstra values 1,3,4,6,7,9,8,12,9,15",
        computed
        == {
            1: (1, 3),
            2: (4, 6),
            3: (7, 9),
            4: (8, 12),
            5: (9, 15),
        },
    )
    checks.check(
        "theorem-2-k1",
        "t(1,0,0)^2/1^2 > t(1,1,1)^2/(3*1^2) fails (3 > 9 is false)",
        (not reverse_by_k[1]) and rows[0][3] == 3 and rows[0][4] == 9,
    )
    checks.check(
        "theorem-2-k2",
        "t(2,0,0)^2/2^2 > t(2,2,2)^2/(3*2^2) holds (48 > 36)",
        reverse_by_k[2] and rows[1][3] == 48 and rows[1][4] == 36,
    )
    checks.check(
        "theorem-2-k3",
        "t(3,0,0)^2/3^2 > t(3,3,3)^2/(3*3^2) holds (147 > 81)",
        reverse_by_k[3] and rows[2][3] == 147 and rows[2][4] == 81,
    )
    checks.check(
        "theorem-2-k4",
        "t(4,0,0)^2/4^2 > t(4,4,4)^2/(3*4^2) holds (192 > 144)",
        reverse_by_k[4] and rows[3][3] == 192 and rows[3][4] == 144,
    )
    checks.check(
        "theorem-2-k5",
        "t(5,0,0)^2/5^2 > t(5,5,5)^2/(3*5^2) holds (243 > 225)",
        reverse_by_k[5] and rows[4][3] == 243 and rows[4][4] == 225,
    )
    checks.check(
        "not-all-scales-reverse",
        "the cheaper rival does not keep same-k reverse at every k=1..5",
        (not reverse_by_k[1])
        and reverse_by_k[2]
        and reverse_by_k[3]
        and reverse_by_k[4]
        and reverse_by_k[5],
    )
    checks.check(
        "one-dijkstra",
        "exactly one origin Dijkstra assigned a finite time to every ball site",
        DIJKSTRA_CALLS == 1
        and len(distances) == len(sites)
        and all(distances[site] >= 0 for site in sites),
    )
    checks.check(
        "note-reports-times",
        "the note reports the ten computed times",
        "t(1,0,0)=1" in note
        and "t(1,1,1)=3" in note
        and "t(2,0,0)=4" in note
        and "t(2,2,2)=6" in note
        and "t(3,0,0)=7" in note
        and "t(3,3,3)=9" in note
        and "t(4,0,0)=8" in note
        and "t(4,4,4)=12" in note
        and "t(5,0,0)=9" in note
        and "t(5,5,5)=15" in note,
    )
    checks.check(
        "note-reports-reverse-products",
        "the note records the five integer reverse products",
        "3 > 9" in note
        and "48 > 36" in note
        and "147 > 81" in note
        and "192 > 144" in note
        and "243 > 225" in note
        and "is false" in note,
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
        "no-axiom-edit",
        "note records hypothetical axiom status no edit",
        'hypothetical_axiom_status: "no edit"' in note,
    )
    checks.check(
        "claim-scope",
        "the note states the required claim_scope",
        "Axis and body-diagonal arrival ratios under the named (0,1,1) hop-cost on B_16(0) are reported"
        in note,
    )
    forbidden = tuple("".join(parts) for parts in FORBIDDEN_PARTS)
    forbidden_hits = [token for token in forbidden if token in note]
    checks.check(
        "forbidden-tokens",
        "the note avoids the forbidden tokens",
        forbidden_hits == [],
    )
    checks.check(
        "uniqueness-not-required",
        "the note does not claim uniqueness of the named rule",
        "Uniqueness is not required" in note
        and "unique hop-cost" not in note,
    )
    checks.check(
        "same-k-not-doubled-pairing",
        "the note scores same-k pairs, not the doubled pairing",
        "same-`k`" in note
        and "not the doubled pairing" in note
        and "(8,0,0)" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
