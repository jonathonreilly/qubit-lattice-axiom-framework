#!/usr/bin/env python3
"""Score same-k axis/body-diagonal ratios under ν on B_12(0).

One origin Dijkstra. No cache write. No axiom edit.
"""

from __future__ import annotations

import ast
import heapq
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/SUPPORT_DROP_SCALE_RATIOS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SUPPORT_DROP_SCALE_RATIOS_B12_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
CLAIM_SCOPE = (
    "Axis and body-diagonal arrival ratios under the named "
    "support-drop hop-cost on B_12(0) are reported for k=1..4. "
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
# (k, t(k,0,0), t(k,k,k))
REPORTED = ((1, 3, 5), (2, 6, 8), (3, 9, 11), (4, 10, 14))
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


def alpha_cost(v: tuple[int, int, int], w: tuple[int, int, int]) -> int:
    sigma_v = support_size(v)
    sigma_w = support_size(w)
    if sigma_v == 0 or (sigma_v == 1 and sigma_w == 1):
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
        "not written into Admissibility" in note,
    )
    checks.check(
        "not-attach-l1",
        "the displayed rule is not attached to L1",
        "not attached to L1" in note and "Do not attach L1" not in axiom,
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
    dist = dijkstra_nu(sites)
    print(f"n_sites {len(sites)}")
    print(f"dijkstra_calls {DIJKSTRA_CALLS}")

    times: dict[int, tuple[int, int]] = {}
    all_reverse = True
    for k, t_axis_rep, t_body_rep in REPORTED:
        t_axis = dist[(k, 0, 0)]
        t_body = dist[(k, k, k)]
        times[k] = (t_axis, t_body)
        reverse = 3 * t_axis * t_axis > t_body * t_body
        all_reverse = all_reverse and reverse
        print(
            f"k {k} t({k},0,0) {t_axis} t({k},{k},{k}) {t_body} "
            f"3t_axis^2 {3 * t_axis * t_axis} t_body^2 {t_body * t_body} "
            f"reverse {reverse}"
        )
        checks.check(
            f"t-k{k}",
            f"t({k},0,0)={t_axis_rep} and t({k},{k},{k})={t_body_rep}",
            t_axis == t_axis_rep and t_body == t_body_rep,
        )
        checks.check(
            f"reverse-k{k}",
            f"t({k},0,0)^2/{k}^2 > t({k},{k},{k})^2/(3*{k}^2)",
            reverse,
        )

    checks.check(
        "one-dijkstra",
        "exactly one Dijkstra ran",
        DIJKSTRA_CALLS == 1,
    )
    checks.check(
        "ball-b12",
        "B_12(0) has 2625 sites and is the ℓ¹ ball of radius 12",
        len(sites) == 2625 and all(l1(v) <= 12 for v in sites),
    )
    checks.check(
        "reachable",
        "every site of B_12(0) is reached",
        len(dist) == 2625,
    )
    checks.check(
        "all-scales-reverse",
        "every k=1..4 same-k pair reverses",
        all_reverse,
    )
    checks.check(
        "note-records-times",
        "note records the eight computed arrivals",
        all(
            f"`{t_axis}`" in note and f"`{t_body}`" in note
            for _k, t_axis, t_body in REPORTED
        )
        and "`(4,0,0)`" in note
        and "`(4,4,4)`" in note,
    )
    checks.check(
        "note-records-reverse-products",
        "note records the four integer reverse products",
        "27 > 25" in note
        and "108 > 64" in note
        and "243 > 121" in note
        and "300 > 196" in note,
    )
    checks.check(
        "not-leftover-of-b8",
        "(3,3,3) and (4,4,4) lie outside B_8(0) and the note says so",
        l1((3, 3, 3)) == 9
        and l1((4, 4, 4)) == 12
        and "outside `B_8(0)`" in note
        and "not a leftover of a `B_8` table" in note,
    )
    checks.check(
        "not-leftover-of-alpha",
        "α cannot price the support-drop hop (1,1,0)→(1,0,0)",
        nu_cost((1, 1, 0), (1, 0, 0)) == 3
        and alpha_cost((1, 1, 0), (1, 0, 0)) == 1
        and "cannot price support drop" in note,
    )
    checks.check(
        "seed-and-axis-clauses",
        "seed-exit and both-weights-1 cost 3; support increase costs 1",
        nu_cost((0, 0, 0), (1, 0, 0)) == 3
        and nu_cost((1, 0, 0), (2, 0, 0)) == 3
        and nu_cost((1, 0, 0), (1, 1, 0)) == 1
        and nu_cost((1, 1, 0), (1, 1, 1)) == 1,
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
