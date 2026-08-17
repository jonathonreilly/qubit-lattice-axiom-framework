#!/usr/bin/env python3
"""Named (0,1,1) hop-cost face reverse versus k on B_16(0).

One Dijkstra from the origin. For each k=1..8 the arrivals t(2k,0,0)
and t(k,k,0) and the displayed reverse bit
t(2k,0,0)^2 / (4k^2) > t(k,k,0)^2 / (2k^2) are reported. Displayed,
not adopted. No axiom edit, no cache write, no L1 hop-cost attachment.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = "CLAUSE_011_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md"
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/CLAUSE_011_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BALL_RADIUS = 16
SCALES = tuple(range(1, 9))
AXIS_TARGETS = tuple((2 * k, 0, 0) for k in SCALES)
FACE_TARGETS = tuple((k, k, 0) for k in SCALES)
TARGETS = AXIS_TARGETS + FACE_TARGETS
NEIGHBOR_STEPS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
FORBIDDEN = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
DIJKSTRA_CALLS = 0

EXPECTED_AXIS = (4, 8, 10, 12, 14, 16, 18, 22)
EXPECTED_FACE = (2, 4, 6, 8, 10, 12, 14, 16)
EXPECTED_REVERSE = (True, True, True, True, False, False, False, False)


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

    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required static literal pair and both files exist",
        AUDIT_INPUT_PATHS
        == (
            "docs/CLAUSE_011_FACE_REVERSE_VS_K_B16_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and audit_paths_are_static_literals()
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )

    sites = ball_sites()
    site_set = set(sites)
    checks.check(
        "ball-b16-only",
        "B_16(0) is the 16-hop neighborhood of the origin and contains every named target",
        len(sites) == 6017
        and all(in_ball(site) for site in TARGETS)
        and (16, 0, 0) in site_set
        and (8, 8, 0) in site_set
        and (17, 0, 0) not in site_set
        and (9, 8, 0) not in site_set
        and nn_radius((8, 8, 0)) == 16
        and nn_radius((16, 0, 0)) == 16,
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
    axis_times = tuple(distances[(2 * k, 0, 0)] for k in SCALES)
    face_times = tuple(distances[(k, k, 0)] for k in SCALES)
    reverse_bits = tuple(
        axis_times[i] * axis_times[i] * (2 * k * k)
        > face_times[i] * face_times[i] * (4 * k * k)
        for i, k in enumerate(SCALES)
    )
    integer_bits = tuple(
        axis_times[i] * axis_times[i] > 2 * face_times[i] * face_times[i]
        for i in range(8)
    )

    for k, t_axis, t_face, bit in zip(SCALES, axis_times, face_times, reverse_bits):
        left = t_axis * t_axis
        right_face = t_face * t_face
        print(
            f"k={k} t({2 * k},0,0)={t_axis} t({k},{k},0)={t_face} "
            f"t_axis^2/(4k^2)={left / (4 * k * k)} "
            f"t_face^2/(2k^2)={right_face / (2 * k * k)} "
            f"{left}>{2 * right_face} reverse={bit}"
        )
    print(f"dijkstra_count=1")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    checks.check(
        "theorem-1-times",
        "the named arrivals are 4,8,10,12,14,16,18,22 on axis and 2,4,6,8,10,12,14,16 on face",
        axis_times == EXPECTED_AXIS and face_times == EXPECTED_FACE,
    )
    checks.check(
        "theorem-2-bits",
        "reverse holds at k=1..4 and fails at k=5..8",
        reverse_bits == EXPECTED_REVERSE and integer_bits == EXPECTED_REVERSE,
    )
    checks.check(
        "keep-k4-not-only-k5",
        "k=4 still reverses; failure is not isolated at k=5",
        reverse_bits[3] is True and reverse_bits[4:] == (False, False, False, False),
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
        "the note reports every computed axis and face time",
        all(f"t({2 * k},0,0)={axis_times[i]}" in note for i, k in enumerate(SCALES))
        and all(f"t({k},{k},0)={face_times[i]}" in note for i, k in enumerate(SCALES)),
    )
    checks.check(
        "note-reports-comparisons",
        "the note reports the eight displayed reverse comparisons",
        "16 > 8" in note
        and "64 > 32" in note
        and "100 > 72" in note
        and "144 > 128" in note
        and "196 > 200" in note
        and "256 > 288" in note
        and "324 > 392" in note
        and "484 > 512" in note,
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
        "Face-diagonal reverse versus integer scale k under the named (0,1,1) hop-cost on B_16(0) is reported for k=1..8"
        in note,
    )
    forbidden_hits = [token for token in FORBIDDEN if token in note]
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

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
