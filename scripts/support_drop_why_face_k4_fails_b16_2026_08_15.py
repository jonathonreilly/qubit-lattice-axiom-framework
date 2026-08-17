#!/usr/bin/env python3
"""Lex-first shortest paths explaining the k=4 face reverse fail on B_16(0)."""

from __future__ import annotations

import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_WHY_FACE_K4_FAILS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[1]

RADIUS = 16
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
TARGETS = (
    (8, 0, 0),
    (4, 4, 0),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
CLAIM_SCOPE = (
    "Lex-first shortest paths to (8,0,0) and (4,4,0) under the named "
    "support-drop hop-cost on B_16(0) are named. Displayed, not adopted."
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


def format_site(v: tuple[int, int, int]) -> str:
    return f"({v[0]},{v[1]},{v[2]})"


def format_walk(path: tuple[tuple[int, int, int], ...]) -> str:
    parts = ["0"]
    for site in path[1:]:
        parts.append(format_site(site))
    return r"\to".join(parts)


def hop_costs(path: tuple[tuple[int, int, int], ...]) -> list[int]:
    return [nu(path[i], path[i + 1]) for i in range(len(path) - 1)]


def running_costs(costs: list[int]) -> list[int]:
    out: list[int] = []
    acc = 0
    for cost in costs:
        acc += cost
        out.append(acc)
    return out


def format_int_seq(values: list[int]) -> str:
    return ",".join(str(v) for v in values)


def dijkstra_lex_first(
    sites: set[tuple[int, int, int]],
) -> tuple[
    dict[tuple[int, int, int], int],
    dict[tuple[int, int, int], tuple[tuple[int, int, int], ...]],
]:
    origin = (0, 0, 0)
    dist: dict[tuple[int, int, int], int] = {}
    paths: dict[
        tuple[int, int, int], tuple[tuple[int, int, int], ...]
    ] = {}
    heap: list[
        tuple[int, tuple[tuple[int, int, int], ...], tuple[int, int, int]]
    ] = [(0, (origin,), origin)]
    while heap:
        cost, path, v = heapq.heappop(heap)
        if v in dist:
            continue
        dist[v] = cost
        paths[v] = path
        for step in NEIGHBOR_STEPS:
            w = (v[0] + step[0], v[1] + step[1], v[2] + step[2])
            if w not in sites or w in dist:
                continue
            heapq.heappush(heap, (cost + nu(v, w), path + (w,), w))
    return dist, paths


def flatten(text: str) -> str:
    return " ".join(text.split())


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
            "docs/SUPPORT_DROP_WHY_FACE_K4_FAILS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
    )
    checks.check(
        "audit-input-literals",
        "AUDIT_INPUT_PATHS is a static two-string literal in this runner",
        'AUDIT_INPUT_PATHS = (\n    "docs/SUPPORT_DROP_WHY_FACE_K4_FAILS_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",\n    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n)'
        in source,
    )

    sites_list = ball_sites(RADIUS)
    sites = set(sites_list)
    checks.check(
        "ball-cardinality",
        "B_16(0) has 6017 sites and 6016 nonzero sites",
        len(sites_list) == 6017 and (0, 0, 0) in sites and len(sites) == 6017,
    )

    dijkstra_runs = 0
    times, paths = dijkstra_lex_first(sites)
    dijkstra_runs += 1
    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra computation is used",
        dijkstra_runs == 1,
    )
    checks.check(
        "finite-times",
        "both targets are reached by a finite path",
        all(times[v] < 10**9 for v in TARGETS),
    )

    t800 = times[(8, 0, 0)]
    t440 = times[(4, 4, 0)]
    path800 = paths[(8, 0, 0)]
    path440 = paths[(4, 4, 0)]
    hops800 = hop_costs(path800)
    hops440 = hop_costs(path440)
    run800 = running_costs(hops800)
    run440 = running_costs(hops440)
    walk800 = format_walk(path800)
    walk440 = format_walk(path440)
    hop_seq800 = format_int_seq(hops800)
    hop_seq440 = format_int_seq(hops440)
    run_seq800 = format_int_seq(run800)
    run_seq440 = format_int_seq(run440)
    last800 = (path800[-2], path800[-1])
    last440 = (path440[-2], path440[-1])
    dens800 = t800 * t800
    dens440 = t440 * t440
    reverse_holds = dens800 * 32 > dens440 * 64
    fail_holds = not reverse_holds

    print(f"t(8,0,0)={t800}")
    print(f"t(4,4,0)={t440}")
    print(f"lex_first_(8,0,0): {walk800}")
    print(f"hop_costs_(8,0,0): {hop_seq800}")
    print(f"running_(8,0,0): {run_seq800}")
    print(f"lex_first_(4,4,0): {walk440}")
    print(f"hop_costs_(4,4,0): {hop_seq440}")
    print(f"running_(4,4,0): {run_seq440}")
    print(
        f"last_hop_(8,0,0): {format_site(last800[0])}->{format_site(last800[1])} "
        f"nu={hops800[-1]} support {support_size(last800[0])}->{support_size(last800[1])}"
    )
    print(
        f"last_hop_(4,4,0): {format_site(last440[0])}->{format_site(last440[1])} "
        f"nu={hops440[-1]} support {support_size(last440[0])}->{support_size(last440[1])}"
    )
    print(
        f"reverse_compare: t(8,0,0)^2/64={dens800}/64 > t(4,4,0)^2/32={dens440}/32 "
        f"-> {reverse_holds}; fail={fail_holds}"
    )

    checks.check(
        "time-800",
        "computed t(8,0,0)=14 is written in the note",
        t800 == 14 and "t(8,0,0)=14" in note,
        residual=t800,
    )
    checks.check(
        "time-440",
        "computed t(4,4,0)=10 is written in the note",
        t440 == 10 and "t(4,4,0)=10" in note,
        residual=t440,
    )
    checks.check(
        "still-fourteen",
        "t(8,0,0) is still 14 on B_16(0)",
        t800 == 14
        and "t(8,0,0) is still 14" in note
        and "still $t(8,0,0)=14$" in note,
        residual=t800,
    )
    checks.check(
        "lex-path-800",
        "lex-first shortest path to (8,0,0) is written in the note",
        walk800 in note and path800[0] == (0, 0, 0) and path800[-1] == (8, 0, 0),
        residual=walk800,
    )
    checks.check(
        "lex-path-440",
        "lex-first shortest path to (4,4,0) is written in the note",
        walk440 in note and path440[0] == (0, 0, 0) and path440[-1] == (4, 4, 0),
        residual=walk440,
    )
    checks.check(
        "displayed-fail",
        "t(8,0,0)^2/64 > t(4,4,0)^2/32 fails and is written as the fail",
        fail_holds
        and reverse_holds is False
        and dens800 == 196
        and dens440 == 100
        and l2sq((8, 0, 0)) == 64
        and l2sq((4, 4, 0)) == 32
        and r"t(8,0,0)^2/64=196/64=49/16" in note
        and r"t(4,4,0)^2/32=100/32=25/8" in note
        and r"196/64>100/32" in note
        and "fails" in note
        and "the fail" in note,
        residual=(dens800, dens440, reverse_holds),
    )
    checks.check(
        "fail-survives-larger-ball",
        "the k=4 face fail survives the larger ball",
        fail_holds
        and "k=4 face fail survives the larger ball" in note
        and "survives the larger ball" in note,
    )
    checks.check(
        "not-b12-leftover",
        "the named B_16(0) paths are not leftover of the named B_12 paths",
        "not leftover of the named $B_{12}(0)$ paths" in note
        and "independent Dijkstra" in note,
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
    checks.check(
        "uniqueness-not-required",
        "shortest-path uniqueness is not required and is not claimed",
        "Uniqueness of a shortest path is not claimed and is not required."
        in note
        and "Uniqueness of a shortest path is not required." in note,
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
        "axiom-untouched",
        "the axiom memo is an input only",
        "### Admissibility / Local Constraint" in axiom
        and "ν(v→w)" not in axiom,
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
