#!/usr/bin/env python3
"""Named (0,1,1) same-k reverse at k=6 on B_18(0).

One Dijkstra from the origin. Displayed, not adopted. No axiom edit,
no cache write, no L1 hop-cost attachment.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = "CLAUSE_011_SAMEK_K6_B18_BOUNDED_THEOREM_NOTE_2026-08-15.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_SAMEK_K6_B18_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BALL_RADIUS = 18
SCALE = 6
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
        raise RuntimeError("Dijkstra did not reach every site of B_18(0)")
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
        "rule on the finite 18-hop neighborhood B_18(0)"
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
            "docs/CLAUSE_011_SAMEK_K6_B18_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals()
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites()
    axis_site = (SCALE, 0, 0)
    body_site = (SCALE, SCALE, SCALE)
    checks.check(
        "ball-b18-only",
        "B_18(0) is the 18-hop neighborhood of the origin and contains both named targets",
        len(sites) == 8473
        and in_ball(axis_site)
        and in_ball(body_site)
        and body_site in sites
        and (18, 0, 0) in set(sites)
        and (19, 0, 0) not in set(sites)
        and nn_radius(body_site) == 18
        and nn_radius(axis_site) == 6
        and nn_radius((5, 5, 5)) == 15
        and not (nn_radius(body_site) <= 16),
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
    t_axis = distances[axis_site]
    t_body = distances[body_site]
    left = 3 * t_axis * t_axis
    right = t_body * t_body
    reverse = left > right
    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")
    print("dijkstra_count=1")
    print(
        f"k {SCALE} t({SCALE},0,0)={t_axis} t({SCALE},{SCALE},{SCALE})={t_body} "
        f"t_axis^2/36={t_axis * t_axis}/36 t_body^2/108={t_body * t_body}/108 "
        f"3t_axis^2={left} t_body^2={right} reverse={reverse}"
    )

    checks.check(
        "theorem-1-times",
        "the same-k arrival times are the Dijkstra values t(6,0,0)=10 and t(6,6,6)=18",
        t_axis == 10 and t_body == 18,
    )
    checks.check(
        "theorem-2-k6",
        "t(6,0,0)^2/36 > t(6,6,6)^2/108 fails (300 > 324 is false)",
        (not reverse)
        and t_axis * t_axis == 100
        and t_body * t_body == 324
        and left == 300
        and right == 324,
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
        "the note reports the two computed times",
        "t(6,0,0)=10" in note and "t(6,6,6)=18" in note,
    )
    checks.check(
        "note-reports-reverse-products",
        "the note records the displayed k=6 reverse comparison",
        "100/36" in note
        and "324/108" in note
        and "300 > 324" in note
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
        "Same-k reverse at k=6 under the named (0,1,1) hop-cost on B_18(0) is reported"
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
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1" in note and "Do not attach L1" not in axiom,
    )
    checks.check(
        "k6-needs-b18",
        "the k=6 body-diagonal site is absent from B_16(0) and present on B_18(0)",
        nn_radius(body_site) == 18
        and "B_18(0)" in note
        and "(6,6,6)" in note
        and "absent from `B_16(0)`" in note,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
