#!/usr/bin/env python3
"""Face-diagonal reverse versus integer scale k under the named support-drop hop-cost on B_16(0)."""

from __future__ import annotations

import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

RADIUS = 16
SCALES = (1, 2, 3, 4, 5, 6, 7, 8)
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    "Face-diagonal reverse versus integer scale k under the named "
    "support-drop hop-cost on B_16(0) is reported for k=1..8. "
    "Displayed, not adopted."
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


def flatten(text: str) -> str:
    return " ".join(text.split())


def axis_site(k: int) -> tuple[int, int, int]:
    return (2 * k, 0, 0)


def face_site(k: int) -> tuple[int, int, int]:
    return (k, k, 0)


def is_reverse(
    times: dict[tuple[int, int, int], int],
    k: int,
) -> bool:
    axis = axis_site(k)
    face = face_site(k)
    ta = times[axis]
    tb = times[face]
    return ta * ta * l2sq(face) > tb * tb * l2sq(axis)


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
            "docs/SUPPORT_DROP_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "audit-input-literals",
        "AUDIT_INPUT_PATHS is a static two-string literal in this runner",
        'AUDIT_INPUT_PATHS = (\n    "docs/SUPPORT_DROP_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )

    sites_list = ball_sites(RADIUS)
    sites = set(sites_list)
    checks.check(
        "ball-cardinality",
        "B_16(0) has 6017 sites and 6016 nonzero sites",
        len(sites_list) == 6017 and (0, 0, 0) in sites and len(sites) == 6017,
    )

    targets = tuple(axis_site(k) for k in SCALES) + tuple(face_site(k) for k in SCALES)
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
        all(times[v] < 10**9 for v in targets),
    )

    expected_times = {
        (2, 0, 0): 6,
        (4, 0, 0): 10,
        (6, 0, 0): 12,
        (8, 0, 0): 14,
        (10, 0, 0): 16,
        (12, 0, 0): 18,
        (14, 0, 0): 20,
        (16, 0, 0): 24,
        (1, 1, 0): 4,
        (2, 2, 0): 6,
        (3, 3, 0): 8,
        (4, 4, 0): 10,
        (5, 5, 0): 12,
        (6, 6, 0): 14,
        (7, 7, 0): 16,
        (8, 8, 0): 18,
    }
    print("arrival_times:")
    for k in SCALES:
        for v in (axis_site(k), face_site(k)):
            print(f"  t{v}={times[v]}  t^2/|v|_2^2={times[v] ** 2}/{l2sq(v)}")

    for v, expected in expected_times.items():
        token = f"t({v[0]},{v[1]},{v[2]})={expected}"
        checks.check(
            f"time-{v[0]}{v[1]}{v[2]}",
            f"computed {token} is written in the note",
            token in note and times[v] == expected,
            residual=times[v],
        )

    expected_bits = {
        1: True,
        2: True,
        3: True,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
    }
    comparison_tokens = {
        1: r"4\,t(1,1,0)^2=64<72=2\,t(2,0,0)^2",
        2: r"16\,t(2,2,0)^2=576<800=8\,t(4,0,0)^2",
        3: r"36\,t(3,3,0)^2=2304<2592=18\,t(6,0,0)^2",
        4: r"64\,t(4,4,0)^2=6400>6272=32\,t(8,0,0)^2",
        5: r"100\,t(5,5,0)^2=14400>12800=50\,t(10,0,0)^2",
        6: r"144\,t(6,6,0)^2=28224>23328=72\,t(12,0,0)^2",
        7: r"196\,t(7,7,0)^2=50176>39200=98\,t(14,0,0)^2",
        8: r"256\,t(8,8,0)^2=82944>73728=128\,t(16,0,0)^2",
    }
    print("reverse_bits:")
    bits: list[bool] = []
    for k in SCALES:
        axis = axis_site(k)
        face = face_site(k)
        bit = is_reverse(times, k)
        bits.append(bit)
        ta, tb = times[axis], times[face]
        print(
            f"  k={k} {axis} vs {face}: reverse={bit} "
            f"({tb * tb}*{l2sq(axis)}={tb * tb * l2sq(axis)} vs "
            f"{ta * ta}*{l2sq(face)}={ta * ta * l2sq(face)})"
        )
        dens_ok = ta * ta * (2 * k * k) > tb * tb * (4 * k * k)
        checks.check(
            f"reverse-k{k}",
            f"k={k} reverse bit is {expected_bits[k]} and the comparison is written",
            bit is expected_bits[k]
            and dens_ok is expected_bits[k]
            and comparison_tokens[k] in note,
        )

    checks.check(
        "fail-not-only-at-k45",
        "reverse fails at k=4,5,6,7,8, so the fail does not stay only at k=4,5",
        bits == [True, True, True, False, False, False, False, False]
        and "does not stay only at $k=4,5$" in note
        and "fails at $k=4,5,6,7,8$" in note,
    )
    checks.check(
        "not-b12-leftover",
        "the k=1..8 census is not leftover of the B_12(0) facek table",
        "not leftover of the $B_{12}(0)$" in note
        and "independent Dijkstra" in note
        and times[(12, 0, 0)] == 18
        and times[(12, 0, 0)] != 20
        and times[(16, 0, 0)] == 24
        and times[(7, 7, 0)] == 16
        and times[(8, 8, 0)] == 18
        and l1((14, 0, 0)) == 14
        and l1((16, 0, 0)) == 16
        and l1((8, 8, 0)) == 16
        and l1((14, 0, 0)) > 12
        and l1((7, 7, 0)) > 12,
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
    checks.check(
        "pair-reverse-bits",
        "the eight declared scales have the displayed reverse bits",
        tuple(bits) == (True, True, True, False, False, False, False, False),
        residual=bits,
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
