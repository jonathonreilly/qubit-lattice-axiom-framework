#!/usr/bin/env python3
"""Named (0,1,1) body-diagonal reverse versus scale k on B_16(0).

One Dijkstra from the origin. Displayed, not adopted. No axiom edit,
no cache write, no L1 hop-cost attachment.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = "CLAUSE_011_BODY_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_BODY_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CLAIM_SCOPE = (
    "Body-diagonal reverse versus integer scale k under the "
    "named (0,1,1) hop-cost on B_16(0) is reported for k=1..5. "
    "Displayed, not adopted."
)

BALL_RADIUS = 16
SCALES = (1, 2, 3, 4, 5)
# (k, t(2k,0,0), t(k,k,k), reverse)
REPORTED = (
    (1, 4, 3, True),
    (2, 8, 6, True),
    (3, 10, 9, False),
    (4, 12, 12, False),
    (5, 14, 15, False),
)
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
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
    print(f"claim_scope: {CLAIM_SCOPE}")
    print("cache_write: false")

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static literal pair and both files exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_BODY_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals()
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites()
    named_targets = tuple((2 * k, 0, 0) for k in SCALES) + tuple(
        (k, k, k) for k in SCALES
    )
    checks.check(
        "ball-b16-only",
        "B_16(0) is the 16-hop neighborhood of the origin and contains every named target",
        len(sites) == 6017
        and all(in_ball(site) for site in named_targets)
        and (10, 0, 0) in sites
        and (5, 5, 5) in sites
        and (17, 0, 0) not in set(sites),
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
    print("dijkstra_count=1")

    all_match = True
    for k, t_axis_rep, t_body_rep, reverse_rep in REPORTED:
        t_axis = distances[(2 * k, 0, 0)]
        t_body = distances[(k, k, k)]
        lhs = 12 * t_axis * t_axis
        rhs = 16 * t_body * t_body
        reverse = lhs > rhs
        all_match = all_match and reverse == reverse_rep
        print(
            f"k {k} t({2 * k},0,0)={t_axis} t({k},{k},{k})={t_body} "
            f"12 t(2k,0,0)^2={lhs} 16 t(k,k,k)^2={rhs} reverse={reverse}"
        )
        checks.check(
            f"theorem-1-k{k}",
            f"t({2 * k},0,0)={t_axis_rep} and t({k},{k},{k})={t_body_rep}",
            t_axis == t_axis_rep and t_body == t_body_rep,
        )
        checks.check(
            f"theorem-2-k{k}",
            f"12 t({2 * k},0,0)^2 > 16 t({k},{k},{k})^2 is {reverse_rep}",
            reverse == reverse_rep and (lhs > rhs) == reverse,
        )

    checks.check(
        "one-dijkstra",
        "exactly one origin Dijkstra assigned a finite time to every ball site",
        DIJKSTRA_CALLS == 1
        and len(distances) == len(sites)
        and all(distances[site] >= 0 for site in sites),
    )
    checks.check(
        "reverse-bits-match",
        "computed reverse bits match the five-scale census yes,yes,no,no,no",
        all_match,
    )
    checks.check(
        "note-reports-times",
        "the note reports the ten computed times and the five displayed comparisons",
        "t(2,0,0)=4" in note
        and "t(1,1,1)=3" in note
        and "t(4,0,0)=8" in note
        and "t(2,2,2)=6" in note
        and "t(6,0,0)=10" in note
        and "t(3,3,3)=9" in note
        and "t(8,0,0)=12" in note
        and "t(4,4,4)=12" in note
        and "t(10,0,0)=14" in note
        and "t(5,5,5)=15" in note
        and "192 > 144" in note
        and "768 > 576" in note
        and "1200 > 1296" in note
        and "1728 > 2304" in note
        and "2352 > 3600" in note,
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
        CLAIM_SCOPE in note.replace("\n", " "),
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
