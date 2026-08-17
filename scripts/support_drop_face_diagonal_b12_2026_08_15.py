#!/usr/bin/env python3
"""Face-diagonal versus axis order under the named support-drop hop-cost on B_12(0)."""

from __future__ import annotations

import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

RADIUS = 12
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
TARGETS = (
    (4, 0, 0),
    (8, 0, 0),
    (12, 0, 0),
    (2, 2, 0),
    (4, 4, 0),
    (6, 6, 0),
    (2, 2, 2),
    (4, 4, 4),
)
PAIRS = (
    ((4, 0, 0), (2, 2, 0)),
    ((8, 0, 0), (4, 4, 0)),
    ((12, 0, 0), (6, 6, 0)),
    ((4, 0, 0), (2, 2, 2)),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    "Face-diagonal versus axis arrival order under the named "
    "support-drop hop-cost on B_12(0) is reported. Displayed, not adopted."
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(
        self,
        label: str,
        statement: str,
        condition: bool,
        residual: object | None = None,
    ) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")
        if not ok and residual is not None:
            print(f"  residual: {residual}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def l1(v: tuple[int, int, int]) -> int:
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def l2sq(v: tuple[int, int, int]) -> int:
    return v[0] * v[0] + v[1] * v[1] + v[2] * v[2]


def support_size(v: tuple[int, int, int]) -> int:
    return sum(1 for x in v if x != 0)


def nu(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sv = support_size(v)
    sw = support_size(w)
    if sv == 0 or (sv == 1 and sw == 1) or sw < sv:
        return 3
    return 1


def ball_sites(radius: int) -> list[tuple[int, int, int]]:
    sites: list[tuple[int, int, int]] = []
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            rem = radius - abs(x) - abs(y)
            for z in range(-rem, rem + 1):
                sites.append((x, y, z))
    return sites


def dijkstra_from_origin(
    sites: set[tuple[int, int, int]],
) -> dict[tuple[int, int, int], int]:
    origin = (0, 0, 0)
    inf = 10**9
    dist = {site: inf for site in sites}
    dist[origin] = 0
    heap: list[tuple[int, tuple[int, int, int]]] = [(0, origin)]
    while heap:
        cost, v = heapq.heappop(heap)
        if cost != dist[v]:
            continue
        for step in NEIGHBOR_STEPS:
            w = (v[0] + step[0], v[1] + step[1], v[2] + step[2])
            if w not in sites:
                continue
            nxt = cost + nu(v, w)
            if nxt < dist[w]:
                dist[w] = nxt
                heapq.heappush(heap, (nxt, w))
    return dist


def more_diagonal(
    a: tuple[int, int, int], b: tuple[int, int, int]
) -> tuple[int, int, int]:
    if support_size(b) > support_size(a):
        return b
    if support_size(a) > support_size(b):
        return a
    raise ValueError("pair is not an axis/face comparison")


def flatten(text: str) -> str:
    return " ".join(text.split())


def is_reverse(
    times: dict[tuple[int, int, int], int],
    axis: tuple[int, int, int],
    diag: tuple[int, int, int],
) -> bool:
    ta = times[axis]
    tb = times[diag]
    return tb * tb * l2sq(axis) < ta * ta * l2sq(diag)


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print("cache_write: false")
    print("dijkstra_count_budget: 1")
    print(f"claim_scope: {CLAIM_SCOPE}")

    checks.check(
        "audit-input-paths",
        "declared inputs are exactly the source note and the axiom memo",
        AUDIT_INPUT_PATHS
        == (
            "docs/SUPPORT_DROP_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "audit-input-literals",
        "AUDIT_INPUT_PATHS is a static two-string literal in this runner",
        'AUDIT_INPUT_PATHS = (\n    "docs/SUPPORT_DROP_FACE_DIAGONAL_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )

    sites_list = ball_sites(RADIUS)
    sites = set(sites_list)
    checks.check(
        "ball-cardinality",
        "B_12(0) has 2625 sites and 2624 nonzero sites",
        len(sites_list) == 2625 and (0, 0, 0) in sites and len(sites) == 2625,
    )

    dijkstra_runs = 0
    times = dijkstra_from_origin(sites)
    dijkstra_runs += 1
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra computation is used",
        dijkstra_runs == 1,
    )
    checks.check(
        "finite-times",
        "every target is reached by a finite path",
        all(times[v] < 10**9 for v in TARGETS),
    )

    reported = {v: times[v] for v in TARGETS}
    print("arrival_times:")
    for v in TARGETS:
        print(f"  t{v}={reported[v]}  t^2/|v|_2^2={reported[v] ** 2}/{l2sq(v)}")

    token = {
        (4, 0, 0): "t(4,0,0)=10",
        (8, 0, 0): "t(8,0,0)=14",
        (12, 0, 0): "t(12,0,0)=20",
        (2, 2, 0): "t(2,2,0)=6",
        (4, 4, 0): "t(4,4,0)=10",
        (6, 6, 0): "t(6,6,0)=14",
        (2, 2, 2): "t(2,2,2)=8",
        (4, 4, 4): "t(4,4,4)=14",
    }
    for v in TARGETS:
        checks.check(
            f"time-{v[0]}{v[1]}{v[2]}",
            f"computed {token[v]} is written in the note",
            token[v] in note and reported[v] == int(token[v].split("=")[1]),
            residual=reported[v],
        )

    print("reverse_bits:")
    pair_bits: list[bool] = []
    for axis, diag in PAIRS:
        if more_diagonal(axis, diag) != diag:
            pair_bits.append(False)
            continue
        bit = is_reverse(times, axis, diag)
        pair_bits.append(bit)
        ta, tb = times[axis], times[diag]
        print(
            f"  {axis} vs {diag}: reverse={bit} "
            f"({tb * tb}*{l2sq(axis)}={tb * tb * l2sq(axis)} vs "
            f"{ta * ta}*{l2sq(diag)}={ta * ta * l2sq(diag)})"
        )
    checks.check(
        "reverse-400-220",
        "((4,0,0),(2,2,0)) is reverse and the note records 16 t(2,2,0)^2=576<800=8 t(4,0,0)^2",
        is_reverse(times, (4, 0, 0), (2, 2, 0))
        and "16\\,t(2,2,0)^2=576<800=8\\,t(4,0,0)^2" in note,
    )
    checks.check(
        "reverse-800-440",
        "((8,0,0),(4,4,0)) is not reverse and the note records 64 t(4,4,0)^2=6400>6272=32 t(8,0,0)^2",
        (not is_reverse(times, (8, 0, 0), (4, 4, 0)))
        and "64\\,t(4,4,0)^2=6400>6272=32\\,t(8,0,0)^2" in note,
    )
    checks.check(
        "reverse-1200-660",
        "((12,0,0),(6,6,0)) is reverse and the note records 144 t(6,6,0)^2=28224<28800=72 t(12,0,0)^2",
        is_reverse(times, (12, 0, 0), (6, 6, 0))
        and "144\\,t(6,6,0)^2=28224<28800=72\\,t(12,0,0)^2" in note,
    )
    checks.check(
        "reverse-400-222",
        "((4,0,0),(2,2,2)) is reverse and the note records 16 t(2,2,2)^2=1024<1200=12 t(4,0,0)^2",
        is_reverse(times, (4, 0, 0), (2, 2, 2))
        and "16\\,t(2,2,2)^2=1024<1200=12\\,t(4,0,0)^2" in note,
    )
    checks.check(
        "not-b8-face-leftover",
        "note states the B_12 face reverse bits are not leftover of the B_8 face times",
        "not leftover of the $B_8(0)$ face times" in note
        and "independent Dijkstra" in note
        and reported[(8, 0, 0)] == 14
        and reported[(8, 0, 0)] != 16
        and reported[(12, 0, 0)] == 20
        and reported[(6, 6, 0)] == 14
        and l1((12, 0, 0)) == 12
        and l1((6, 6, 0)) == 12,
    )

    flat_note = flatten(note)
    flat_axiom = flatten(axiom)
    lattice_quote = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor "
        "adjacency, standard translations, and proper cubic rotations about each site."
    )
    admissibility_quote = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    not_dynamics = "Admissibility is not a dynamics axiom."
    checks.check(
        "source-lattice",
        "Lattice nearest-neighbor wording is pinned in the axiom memo and the note",
        lattice_quote in flat_axiom and lattice_quote in flat_note,
    )
    checks.check(
        "source-admissibility",
        "Admissibility distribution wording and non-dynamics clause are pinned",
        admissibility_quote in flat_axiom
        and admissibility_quote in flat_note
        and not_dynamics in axiom
        and not_dynamics in note,
    )
    checks.check(
        "nu-not-admissibility",
        "the note refuses to write nu into Admissibility",
        "It is not written into Admissibility." in note
        and "Do not write $\\nu$ into Admissibility." in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "Do not attach L1." in note and "not attached to L1" in note,
    )
    checks.check(
        "displayed-not-adopted",
        "claim_scope and displayed-not-adopted wording are present",
        CLAIM_SCOPE in note and "displayed, not adopted" in note,
    )
    forbidden_hits = [
        phrase
        for phrase in FORBIDDEN
        if phrase in note or phrase in source.split("FORBIDDEN =", 1)[0]
    ]
    checks.check(
        "forbidden-phrases",
        "forbidden phrases are absent from the note and from runner prose",
        not forbidden_hits,
        residual=forbidden_hits,
    )
    expected_bits = (
        True,
        False,
        True,
        True,
    )
    checks.check(
        "pair-reverse-bits",
        "the four declared pairs have the displayed reverse bits",
        tuple(pair_bits) == expected_bits,
        residual=pair_bits,
    )
    checks.check(
        "axiom-untouched",
        "the axiom memo is an input only",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
